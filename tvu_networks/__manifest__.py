# -*- coding: utf-8 -*-

{
    'name': "TVU Networks",

    'summary': """
        Automatically cancels quotations after their expiration date has passed. 
    """,

    'description': """
        Cancels quotations in the Sales app every night at midnight after their validity date has passed
    """,

    'author': "Odoo",
    'website': "https://www.odoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'data/quotation_auto_cancel.xml', 
    ],

    'demo': [

    ],
}
