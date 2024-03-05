# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api


class FleetCategoryInherited(models.Model):
    _inherit = "fleet.vehicle.model.category"

    max_weight = fields.Float("Max Weight (Kg)")
    max_volume = fields.Float("Max Volume (msq)")

    @api.depends("name", "max_weight", "max_volume")
    def _compute_display_name(self):
        for record in self:
            record_name = record.name
            if record.max_weight and record.max_volume:
                record_name = f"{record.name} ({record.max_weight} Kg), ({record.max_volume} msq)"
            
            record.display_name = record_name
