# -*- coding: utf-8 -*-
# (c) 2015 Incaser Informatica S.L. - Sergio Teruel
# (c) 2015 Incaser Informatica S.L. - Carlos Dauden
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from openerp.tests.common import TransactionCase


class TestPartnerVATSplit(TransactionCase):
    def setUp(self):
        super(TestPartnerVATSplit, self).setUp()
        self.partner = self.env.ref('base.res_partner_1')
        self.partner.vat = 'ES12345678Z'

    def test_partner_vat_split(self):
        self.assertEqual(self.partner.vat_country_code, 'ES')
        self.assertEqual(self.partner.vat_identifier, '12345678Z')
