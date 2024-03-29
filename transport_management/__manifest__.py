# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Transport Management System',
    'depends': [
        "stock",
        "stock_picking_batch",
        "fleet",
    ],
    'data': [
        "security/ir.model.access.csv",

        "views/fleet_category_view.xml",
        "views/dock_view.xml",
        "views/stock_picking_batch_view.xml",
        "views/store_picking_view.xml",
        
        "views/transport_management_menus.xml",
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3'
}
