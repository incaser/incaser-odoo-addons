# -*- coding: utf-8 -*-
# (c) 2015 Incaser Informatica S.L. - Sergio Teruel
# (c) 2015 Incaser Informatica S.L. - Carlos Dauden
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from openerp import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    vat_country_code = fields.Char(compute='_compute_vat_split')
    vat_identifier = fields.Char(compute='_compute_vat_split')

    def _compute_vat_split(self):
        self.vat_country_code = self.vat[:2]
        self.vat_identifier = self.vat[2:]

    @api.onchange('vat_country_code', 'vat_identifier')
    def _onchange_vat_split(self):
        self.vat = '%s%s' % (self.vat_country_code, self.vat_identifier)
