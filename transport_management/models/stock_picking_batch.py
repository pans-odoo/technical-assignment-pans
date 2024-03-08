# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api
from odoo.exceptions import ValidationError


class StockPickingBatchInherited(models.Model):
    _inherit = "stock.picking.batch"

    dock_id = fields.Many2one(comodel_name="dock", string="Dock Name")
    vehicle_id = fields.Many2one(comodel_name="fleet.vehicle", string="Vehicle")
    vehicle_category_id = fields.Many2one(comodel_name="fleet.vehicle.model.category", string="Vehicle Category")
    weight = fields.Float(string="Weight", compute="_compute_metrics", store=True)
    volume = fields.Float(string="Volume", compute="_compute_metrics", store=True)
    transfer = fields.Integer(string="Transfer", compute="_compute_transfer", store=True)
    line = fields.Integer(string="Line", compute="_compute_line", store=True)
    total_weight= fields.Integer(string="Total weight", compute="_compute_metrics", store=True)
    total_volume= fields.Integer(string="Total Volume", compute="_compute_metrics", store=True)

    @api.onchange("vehicle_id")
    def _onchange_vehicle_category(self):
        self.vehicle_category_id = self.vehicle_id.category_id

    @api.depends("vehicle_category_id", "picking_ids")
    def _compute_metrics(self):
        for rec in self:
            if rec.picking_ids and rec.vehicle_category_id:
                rec.total_weight = sum(rec.picking_ids.mapped("weight"))
                rec.total_volume = sum(rec.picking_ids.mapped("volume"))

                rec.weight = (rec.total_weight/rec.vehicle_category_id.max_weight) * 100
                rec.volume = (rec.total_volume/rec.vehicle_category_id.max_volume) * 100
            else:
                rec.total_weight = 0.0
                rec.total_volume = 0.0
                rec.weight = 0.0
                rec.volume = 0.0

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

    @api.constrains("total_weight")
    def _contrain_weight(self):
        for record in self:
            if(record.total_weight > record.vehicle_category_id.max_weight):
                raise ValidationError("total weight should not be more than the max weight")