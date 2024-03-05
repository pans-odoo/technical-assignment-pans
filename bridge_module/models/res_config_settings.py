# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class ResConfigSettingsInherited(models.TransientModel):
    _inherit = 'res.config.settings'

    module_transport_management = fields.Boolean("Transport Management System")