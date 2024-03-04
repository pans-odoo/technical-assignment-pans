# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api


class StockPickingInherited(models.Model):
    _inherit = "stock.picking"
    
    weight = fields.Float(related="product_id.weight", string="Weight")
    volume = fields.Float(related="product_id.volume", string="Volume")

