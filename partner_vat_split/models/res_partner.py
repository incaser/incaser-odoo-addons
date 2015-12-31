# -*- coding: utf-8 -*-
# (c) 2015 Incaser Informatica S.L. - Sergio Teruel
# (c) 2015 Incaser Informatica S.L. - Carlos Dauden
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from openerp import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    vat_country_code = fields.Char(size=2)
    vat_identifier = fields.Char()

    # @api.onchange('vat')
    # def _compute_vat_split(self):
    #     for partner in self:
    #         if partner.vat:
    #             partner.vat_country_code = partner.vat[:2]
    #             partner.vat_identifier = partner.vat[2:]

    @api.onchange('vat_country_code', 'vat_identifier')
    def _onchange_vat_split(self):
        for partner in self:
            if partner.vat_country_code:
                partner.vat = '%s%s' % (
                    partner.vat_country_code, partner.vat_identifier)

    @api.multi
    def vat_change(self, value):
        res = super(ResPartner, self).vat_change(value)
        if value:
            res['vat_country_code'] = value[:2]
            res['vat_identifier'] = value[2:]
        # for partner in self:
        #     if partner.vat:
        #         partner.vat_country_code = partner.vat[:2]
        #         partner.vat_identifier = partner.vat[2:]
        return res
