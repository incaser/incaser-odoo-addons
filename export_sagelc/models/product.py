# -*- coding: utf-8 -*-
# (c) 2015 Incaser Informatica S.L. - Sergio Teruel
# (c) 2015 Incaser Informatica S.L. - Carlos Dauden
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from openerp import models, fields, api
from openerp.tools.float_utils import float_round

tipo_articulo = {'product': 'M', 'consu': 'M', 'service': 'I'}

class ProductProduct(models.Model):
    _inherit = 'product.product'

    sagelc_export = fields.Boolean(string='Exported')
    sagelc_code = fields.Char(string='SageLC Code', size=15)

    @api.multi
    def export_records(self):
        db_obj = self.env['base.external.dbsource']
        db_sage = db_obj.search([('name', '=', 'Logic')])
        for product in self.with_context(pricelist=1):
            product_code = 'od' + str(product.id).zfill(5)
            dic_equiv = {
                         'CodigoEmpresa': 0,
                         'CodigoArticulo': product_code,
                         'DescripcionArticulo': product.name,
                         'ComentarioArticulo': product.description or '',
                         'DescripcionLinea': product.description_sale or '',
                         'CodigoAlternativo': product.ean13 or '',
                         'CodigoAlternativo2': product.default_code or '',
                         'TipoArticulo': tipo_articulo[product.type],
                         'ValoracionStock': 2,
                         'GrupoIva': 1,
                         'GrupoIvaCompras': 1,
                         'PrecioCompra': product.standard_price,
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