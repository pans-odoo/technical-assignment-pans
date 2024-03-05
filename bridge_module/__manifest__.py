# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Bridge Module',
    'depends': [
        "stock"
    ],
    'data': [
        # "security/ir.model.access.csv",
        "views/res_config_setting_view.xml",
        
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3'
}
