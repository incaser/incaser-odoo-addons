# -*- coding: utf-8 -*-
# (c) 2015 Incaser Informatica S.L. - Sergio Teruel
# (c) 2015 Incaser Informatica S.L. - Carlos Dauden
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from openerp import models, fields


class HrTimesheetInvoiceCreate(models.TransientModel):
    _inherit = 'hr.timesheet.invoice.create'

    date_invoice = fields.Date()
