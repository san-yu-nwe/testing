# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Inline Discount(Percentage/Amount)',
    'category': 'Sales/Sales',
    'summary': 'Inline Discount in Sales Module',
    'description': """
This module provide to give discount in both percentage and amount form in the sales invoice.
This is a version 1.1.
    """,
    'depends': ['sale','account'],
    'data': [
        'views/sale_internal.xml',
        'views/account_invoices.xml'
    ],
    'demo': [

    ],
    'qweb': [

    ],
    'installable': True,
    'auto_install': False
}
