# -*- coding: utf-8 -*-

{
    'name': 'Odoo Academy',
    
    'summary': 'Academy app to manage Training',
    
    'description': """
        Academy Module to manage Training:
        - Courses
        - Sessions
        - Attendees
    """,
    
    'author': 'Odoo',
    
    'website': 'https://www.odoo.com',
    
    'category': 'Training',
    'version': '0.1',
    
    'depends': ['base'],
    
    'data': [
        'security/academy_security.xml', # Make sure to load the xml file first. The groups need to be loaded before the access rights
        'security/ir.model.access.csv'
    ],
    
    'demo': [
        'demo/academy_demo.xml'
    ],
}