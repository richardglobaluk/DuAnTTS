# -*- coding: utf-8 -*-
{
    'name': "cptuanhuy_coa",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "VietERP/Vu",
    'website': "http://www.vieterp.net",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'clickable_chartofaccount'],
    'qweb': [
        'static/src/xml/account_account_tree.xml',
    ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/account_account.xml'
    ],
    # only loaded in demonstration mode
}