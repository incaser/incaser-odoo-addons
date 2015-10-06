# -*- coding: utf-8 -*-
# (c) 2015 Incaser Informatica S.L. - Sergio Teruel
# (c) 2015 Incaser Informatica S.L. - Carlos Dauden
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    "name" : "Timesheet Invoice Date",
    "version" : "8.0.1.0",
    "author" : "Incaser Informatica S.L.",
    "category": 'Invoice',
    'complexity': "easy",
    "description": """
Timesheet Invoice Date
======================
This modules add invoice_date in wizard invoice create
    """,
    'website': 'http://www.incaser.es',
    'depends': ['hr_timesheet_invoice'],
    'init_xml': [],
    'data': ['wizard/hr_timesheet_invoice_create_final_view.xml'],
    'demo_xml': [],
    'test': [],
    'application': False,
    'installable': True,
}

