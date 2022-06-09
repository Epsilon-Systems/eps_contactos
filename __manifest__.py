# -*- coding: utf-8 -*-
{
    'name': "KYC",

    'summary': """
        Know Your Customer Module""",

    'description': """
        Module that adds fields to the contact form for PLD and FT in the financial sector
    """,

    'author': "Epsilon Systems",
    'website': "http://www.epsilonsystemsgroup.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Administration',
    'version': '15.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'installable': True,
}
