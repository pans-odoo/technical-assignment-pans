# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api


class StockPickingInherited(models.Model):
    _inherit = "stock.picking"
    
    weight = fields.Float(string="Weight", compute="_compute_weight")
    volume = fields.Float(string="Volume", compute="_compute_volume")
    transfer_lines = fields.Integer(string="Transfer Lines", compute="_compute_transfer_lines")

    api.depends("move_ids")
    def _compute_weight(self):
        for record in self:
            if record.move_ids:
                total_weight = 0
                for line in record.move_ids:
                    total_weight += line.product_id.weight
        
            record.weight = total_weight

    @api.depends("move_ids")
    def _compute_volume(self):
        for record in self:
            if record.move_ids:
                total_volume = 0
                for line in record.move_ids:
                    total_volume += line.product_id.volume

            record.volume = total_volume

    def _compute_transfer_lines(self):
        self.transfer_lines = len(self.move_line_ids)