# -*- coding: utf-8 -*-
# (c) 2015 Incaser Informatica S.L. - Sergio Teruel
# (c) 2015 Incaser Informatica S.L. - Carlos Dauden
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from openerp import models, fields, api
from openerp.tools.float_utils import float_round


class ResPartner(models.Model):
    _inherit = 'res.partner'

    sagelc_customer_ref = fields.Char(string='Sage Customer Ref')
    sagelc_supplier_ref = fields.Char(string='Sage Supplier Ref')

    @api.multi
    def export_records(self):
        db_obj = self.env['base.external.dbsource']
        db_sage = db_obj.search([('name', '=', 'Logic')])
        for partner in self:
            dic_equiv = {
                         'CodigoEmpresa': 0,
                         'EjercicioAlbaran': invoice.date_invoice[:4],
                         'SerieAlbaran': '',
                         'NumeroAlbaran': invoice.id,
                         'IdDelegacion': 'CAS',
                         'CodigoCliente': invoice.partner_id.sagelc_customer_ref,
                         'FechaAlbaran': invoice.date_invoice,
                         'NumeroLineas': len(invoice.invoice_line),
                         'SiglaNacion': invoice.partner_id.vat[:2],
                         'CifDni': invoice.partner_id.vat[3:],
                         'CifEuropeo': invoice.partner_id.vat,
                         'RazonSocial': invoice.partner_id.name,
                         'RazonSocialEnvios': invoice.partner_id.name,
                         'RazonSocial2': invoice.partner_id.name,
                         'RazonSocial2Envios': invoice.partner_id.name,
                         'Nombre': invoice.partner_id.name,
                         'NombreEnvios': invoice.partner_id.name,
                         'Domicilio': invoice.partner_id.street,
                         'DomicilioEnvios': invoice.partner_id.street,
                         'Domicilio2': invoice.partner_id.street2,
                         'Domicilio2Envios': invoice.partner_id.street2,
                         'ViaPublica': invoice.partner_id.street,
                         'CodigoPostal': invoice.partner_id.zip,
                         'CodigoPostalEnvios': invoice.partner_id.zip,
                         'RazonSocialEnvios': invoice.partner_id.name,
                         'CifEuropeo': invoice.partner_id.vat,
                         'CifEuropeo': invoice.partner_id.vat,
                         'CifEuropeo': invoice.partner_id.vat,
                         'CifEuropeo': invoice.partner_id.vat,
                         'CifEuropeo': invoice.partner_id.vat,
                         'PrecioVenta': product.price,
                         '[%Margen]': float_round((product.price - product.standard_price) / product.standard_price * 100, 0),
                         'NumDecimalesUnidades': 2,
                         'TipoABC': 'A',
                         }
            print(dic_equiv)
            key_list = dic_equiv.keys()
            params = '?,' * len(dic_equiv)
            params = params[:-1]
            sql = 'INSERT INTO Articulos (%s) VALUES (%s)' % (', '.join(key_list), params)
            param_list = tuple([dic_equiv[key] for key in key_list])
            db_sage.execute_void(sql, param_list)
            vals = {
                'sagelc_export': True,
                'sagelc_code': product_code
            }
            product.write(vals)