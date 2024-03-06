# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api


class StockPickingInherited(models.Model):
    """inheriting the stock picking model"""
    _inherit = "stock.picking"
    
    weight = fields.Float(string="Weight", compute="_compute_metrics")
    volume = fields.Float(string="Volume", compute="_compute_metrics")
    transfer_lines = fields.Integer(string="Transfer Lines", compute="_compute_transfer_lines")

    api.depends("move_ids")
    def _compute_metrics(self):
        for record in self:
            if record.move_ids:
                total_weight = 0.0
                total_volume = 0.0
                for line in record.move_ids:
                    total_weight += line.product_id.weight
                    total_volume += line.product_id.volume
        
            record.weight = total_weight
            record.volume = total_volume

    def _compute_transfer_lines(self):
        self.transfer_lines = len(self.move_line_ids)