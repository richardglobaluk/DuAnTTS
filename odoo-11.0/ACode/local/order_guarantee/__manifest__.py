# -*- coding: utf-8 -*-
{
    'name': "order_guarantee",

    'summary': """
        order_guarantee
    """,

    'description': """
        order_guarantee
    """,

    'author': "VietERP / Sang",
    'website': "http://www.vieterp.net",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'VietERP',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'account_guarantee',
        'sale',
    ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/sale_order_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}