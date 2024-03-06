# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api


class StockPickingBatchInherited(models.Model):
    _inherit = "stock.picking.batch"

    dock_id = fields.Many2one(comodel_name="dock", string="Dock Name")
    vehicle_id = fields.Many2one(comodel_name="fleet.vehicle", string="Vehicle")
    vehicle_category_id = fields.Many2one(comodel_name="fleet.vehicle.model.category", string="Vehicle Category")
    weight = fields.Float(string="Weight", compute="_compute_metrics", store=True)
    volume = fields.Float(string="Volume", compute="_compute_metrics", store=True)
    transfer = fields.Integer(string="Transfer", compute="_compute_transfer", store=True)
    line = fields.Integer(string="Line", compute="_compute_line", store=True)

    @api.onchange("vehicle_id")
    def update_vehicle_category(self):
        self.vehicle_category_id = self.vehicle_id.category_id

    @api.depends("vehicle_category_id")
    def _compute_metrics(self):
        if self.picking_ids:
            total_weight = sum(self.picking_ids.mapped("weight"))
            total_volume = sum(self.picking_ids.mapped("volume"))

            self.weight = (total_weight/self.vehicle_category_id.max_weight) * 100
            self.volume = (total_volume/self.vehicle_category_id.max_volume) * 100
        else:
            self.weight = 0.0
            self.volume = 0.0

    @api.depends("picking_ids")
    def _compute_transfer(self):
        for record in self:
            record.transfer = len(record.picking_ids)

    @api.depends("move_ids")
    def _compute_line(self):
        for record in self:
            record.line = len(record.move_ids)


    @api.depends('weight', 'volume')
    def _compute_display_name(self):
        for batch in self:
            batch.display_name = f"{batch.name}: {round(batch.weight, 2)}kg, {round(batch.volume, 2)}m\N{SUPERSCRIPT THREE}, {batch.vehicle_id.driver_id.name}"