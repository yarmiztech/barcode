# -*- coding: utf-8 -*-
{
    'name': "Product Barcode Custom",

    'summary': """
        Module is used to create grouped product in odoo.""",

    'description': """
        This module is used to create group which will contain multiple product of similar/disimilar type.
    """,

    'author': "Enzapps",
    'website': "http://www.enzapps.com",
    'images': ['static/description/main.jpg'],
    'category': 'Custom',
    'version': '1.0',
    'depends': ['base', 'product'],

    'data': [
        'reports/report_view.xml'
    ],

}
