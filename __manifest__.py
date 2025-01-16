# -*- coding: utf-8 -*-
{
    'name': "partner_fields",

    'summary': "",

    'description': "",

    'author': "Alejandro Martinez",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale_management','account','hr','contacts'],

    # always loaded
    'data': [
        'views/res_partner_view.xml',
        'views/sale_order_view.xml',
        'views/account_move_view.xml',
        'views/report_invoice_document.xml',
        'views/report_saleorder_template.xml',
    ],
}
