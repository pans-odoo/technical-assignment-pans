# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api

class FleetCategoryInherited(models.Model):
    _inherit = "fleet.vehicle.model.category"

    max_weight = fields.Float("Max Weight (Kg)")
    max_volume = fields.Float("Max Volume (m^3)")

    @api.depends("max_weight", "max_volume")
    def _compute_display_name(self):
        for record in self:
            name = record.name
            if record.max_weight and record.max_volume:
                name = f"{record.name} ({record.max_weight} Kg), ({record.max_volume} m^3)"
            record.display_name = name
