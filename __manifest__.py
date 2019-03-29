# -*- coding: utf-8 -*-
{
    'name': "TDSI-IUT",

    'summary': """
        Module de gestion de parc""",

    'description': """
        Gestion des devices d'une entreprise
    """,

    'author': "teamDSI",
    'website': "http://www.team-dsi.fr",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/iut_it_brand_views.xml',
        'views/iut_it_device_views.xml',
        'views/iut_it_models_views.xml',
        'views/iut_it_partner_views.xml',
        'views/iut_it_type_views.xml',
        'views/iut_it_menu.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}