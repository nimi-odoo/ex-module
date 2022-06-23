# -*- coding: utf-8 -*-
{
    'name': "Real Estate",
    'summary': """
        summ
    """,
    'description': """
        desc
    """,
    'author': "Odoo",
    'website': "https://www.odoo.com",
    'license': 'OPL-1',
    'application': True,
    'category': 'Sales',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        "security/ir.model.access.csv",
        "views/estate_menus.xml",
        "views/estate_property_views.xml",
    ],
    'demo': [],
}
