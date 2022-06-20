# -*- coding: utf-8 -*-

{
    'name': 'Library',
    
    'summary': 'Library app for managing books and customers',
    
    'description': """
        Library Module to manage:
        - Oranizing books and rentals
        - Customers checking out books
    """,
    
    'author': 'Odoo',
    'licence': 'OEPL 1.0',
    'website': 'https://www.odoo.com',
    
    'category': 'Learning',
    'version': '0.1',
    
    'depends': ['base', 'web_map'],
    
    'data': [
        'security/library_security.xml',
        'security/ir.model.access.csv',
        'views/library_menuitem.xml',
        'views/book_views.xml',
        'views/rental_views.xml'
    ],
    
    'demo': [
        'demo/library_demo.xml'
    ],
}