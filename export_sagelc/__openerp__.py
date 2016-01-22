# -*- coding: utf-8 -*-
# (c) 2015 Incaser Informatica S.L. - Sergio Teruel
# (c) 2015 Incaser Informatica S.L. - Carlos Dauden
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    'name': 'Export Logic',
    'summary': 'Export partner, products and invoices to Logic Class-Murano',
    'version': '8.0.1.0.0',
    'category': "Tools",
    'author': 'Incaser Informatica S.L., ',
    'license': 'AGPL-3',
    'depends': ['base_external_dbsource', 'product', 'account'],
    'external_dependencies': {'python': ['pyodbc']},
    'data': [
        'views/export_view.xml',
        'views/product_view.xml',
        'views/res_partner_view.xml',
        'views/account_invoice_view.xml',
    ],
    'installable': True,
}
