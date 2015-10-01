# -*- coding: utf-8 -*-
# (c) 2015 Incaser Informatica S.L. - Sergio Teruel
# (c) 2015 Incaser Informatica S.L. - Carlos Dauden
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from openerp import models, fields, api
from openerp.tools.float_utils import float_round
import decimal

tipo_articulo = {'product': 'M', 'consu': 'M', 'service': 'I'}
codigo_empresa = 1


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    sagelc_export = fields.Boolean(string='Exported')
    sagelc_code = fields.Char(string='SageLC Code', size=15)

    def sanitize_arg(self, val):
        if isinstance(val, decimal.Decimal):
            return eval(str(val)) / 10000000000.0
        else:
            return val

    @api.multi
    def export_records(self):
        if self[0].type == 'out_invoice':
            self.export_records_customer()
        else:
            self.export_records_supplier()

    @api.multi
    def export_records_customer(self):
        db_obj = self.env['base.external.dbsource']
        db_sage = db_obj.search([('name', '=', 'Logic')])
        for invoice in self:
            dic_equiv = {}
            sql = 'SELECT * FROM CabeceraAlbaranCliente WHERE 1=?'
            cab_cols = db_sage.execute(sql, (2), True)['cols']

            sql = 'SELECT * FROM LineasAlbaranCliente WHERE 1=?'
            lin_cols = db_sage.execute(sql, (2), True)['cols']

            sql = 'SELECT * FROM Clientes WHERE CodigoEmpresa=? AND CodigoCliente=?'
            clientes = db_sage.execute(sql, (codigo_empresa, invoice.partner_id.sagelc_customer_ref))
            cli = clientes[0]
            for pos in range(len(cli)):
                col = cli.cursor_description[pos][0]
                if col in cab_cols:
                    dic_equiv['[%s]' % col] = self.sanitize_arg(cli[pos])

            sql = 'SELECT * FROM ClientesConta WHERE CodigoEmpresa=? AND CodigoCuenta=?'
            clientes_conta = db_sage.execute(sql, (codigo_empresa, cli.CodigoContable))
            cli_conta = clientes_conta[0]
            for pos in range(len(cli_conta)):
                col = cli_conta.cursor_description[pos][0]
                if col in cab_cols:
                    dic_equiv['[%s]' % col] = self.sanitize_arg(cli_conta[pos])

            sql = 'SELECT * FROM ClientesProveedores WHERE SiglaNacion=? AND CifDni=?'
            clientes_prov = db_sage.execute(sql, (cli.SiglaNacion, cli.CifDni))
            cli_prov = clientes_prov[0]
            for pos in range(len(cli_prov)):
                col = cli_prov.cursor_description[pos][0]
                if col in cab_cols:
                    dic_equiv['[%s]' % col] = self.sanitize_arg(cli_prov[pos])

            dic_man = {
                '[CodigoEmpresa]': codigo_empresa,
                '[EjercicioAlbaran]': invoice.date_invoice[:4],
                '[SerieAlbaran]': 'OD',
                '[NumeroAlbaran]': invoice.id,
                '[IdDelegacion]': 'CAS',
                '[CodigoCliente]': invoice.partner_id.sagelc_customer_ref,
                '[FechaAlbaran]': invoice.date_invoice,
                '[NumeroLineas]': len(invoice.invoice_line),
                }
            dic_equiv.update(dic_man)
            print(dic_equiv)
            key_list = dic_equiv.keys()
            params = '?,' * len(dic_equiv)
            params = params[:-1]
            sql = 'INSERT INTO CabeceraAlbaranCliente (%s) VALUES (%s)' % (', '.join(key_list), params)
            param_list = tuple([dic_equiv[key] for key in key_list])
            db_sage.execute_void(sql, param_list)
            vals = {'sagelc_export': True}
            invoice.write(vals)

            for line in invoice.invoice_line:
                dic_equiv = {
                    '[CodigoEmpresa]': codigo_empresa,
                    '[EjercicioAlbaran]': invoice.date_invoice[:4],
                    '[SerieAlbaran]': 'OD',
                    '[NumeroAlbaran]': invoice.id,
                    '[Orden]': line.sequence,
                    '[FechaAlbaran]': invoice.date_invoice,
                    '[CodigoArticulo]': line.product_id.sagelc_code,
                    '[CodigoAlmacen]': '1',
                    '[DescripcionArticulo]': line.product_id.name,
                    '[DescripcionLinea]': line.name and line.name.replace('\n', '\r\n') or '',
                    '[FactorConversion_]': 1,
                    '[AcumulaEstadistica_]': -1,
                    '[CodigoTransaccion]': 1,
                    '[GrupoIva]': 1,
                    '[CodigoIva]': 21,
                    '[UnidadesServidas]': line.quantity,
                    '[Unidades]': line.quantity,
                    '[Unidades2_]': line.quantity,
                    '[Precio]': line.price_unit,
                    '[PrecioRebaje]': line.price_unit,
                    '[PrecioCoste]': line.product_id.standard_price,
                    '[%Descuento]': line.discount,
                    '[%Iva]': 21,
                    '[TipoArticulo]': tipo_articulo[line.product_id.type],
                }
                print(dic_equiv)
                key_list = dic_equiv.keys()
                params = '?,' * len(dic_equiv)
                params = params[:-1]
                sql = 'INSERT INTO LineasAlbaranCliente (%s) VALUES (%s)' % (', '.join(key_list), params)
                param_list = tuple([dic_equiv[key] for key in key_list])
                db_sage.execute_void(sql, param_list)

    @api.multi
    def export_records_supplier(self):
        db_obj = self.env['base.external.dbsource']
        db_sage = db_obj.search([('name', '=', 'Logic')])
        codigo_empresa = 1
        for invoice in self:
            dic_equiv = {}
            sql = 'SELECT * FROM CabeceraAlbaranProveedor WHERE 1=?'
            cab_cols = db_sage.execute(sql, (2), True)['cols']

            sql = 'SELECT * FROM LineasAlbaranProveedor WHERE 1=?'
            lin_cols = db_sage.execute(sql, (2), True)['cols']

            sql = 'SELECT * FROM Proveedores WHERE CodigoEmpresa=? AND CodigoProveedor=?'
            proveedores = db_sage.execute(sql, (codigo_empresa, invoice.partner_id.sagelc_supplier_ref))
            prov = proveedores[0]
            for pos in range(len(prov)):
                col = prov.cursor_description[pos][0]
                if col in cab_cols:
                    dic_equiv['[%s]' % col] = self.sanitize_arg(prov[pos])

            sql = 'SELECT * FROM ClientesConta WHERE CodigoEmpresa=? AND CodigoCuenta=?'
            clientes_conta = db_sage.execute(sql, (codigo_empresa, prov.CodigoContable))
            cli_conta = clientes_conta[0]
            for pos in range(len(cli_conta)):
                col = cli_conta.cursor_description[pos][0]
                if col in cab_cols:
                    dic_equiv['[%s]' % col] = self.sanitize_arg(cli_conta[pos])

            sql = 'SELECT * FROM ClientesProveedores WHERE SiglaNacion=? AND CifDni=?'
            clientes_prov = db_sage.execute(sql, (prov.SiglaNacion, prov.CifDni))
            cli_prov = clientes_prov[0]
            for pos in range(len(cli_prov)):
                col = cli_prov.cursor_description[pos][0]
                if col in cab_cols:
                    dic_equiv['[%s]' % col] = self.sanitize_arg(cli_prov[pos])

            dic_man = {
                '[CodigoEmpresa]': codigo_empresa,
                '[EjercicioAlbaran]': invoice.date_invoice[:4],
                '[SerieAlbaran]': 'OD',
                '[NumeroAlbaran]': invoice.id,
                '[IdDelegacion]': 'CAS',
                '[CodigoProveedor]': invoice.partner_id.sagelc_supplier_ref,
                '[FechaAlbaran]': invoice.date_invoice,
                '[NumeroLineas]': len(invoice.invoice_line),
                }
            dic_equiv.update(dic_man)
            print(dic_equiv)
            key_list = dic_equiv.keys()
            params = '?,' * len(dic_equiv)
            params = params[:-1]
            sql = 'INSERT INTO CabeceraAlbaranProveedor (%s) VALUES (%s)' % (', '.join(key_list), params)
            param_list = tuple([dic_equiv[key] for key in key_list])
            db_sage.execute_void(sql, param_list)
            vals = {'sagelc_export': True}
            invoice.write(vals)

            for line in invoice.invoice_line:
                dic_equiv = {
                    '[CodigoEmpresa]': codigo_empresa,
                    '[EjercicioAlbaran]': invoice.date_invoice[:4],
                    '[SerieAlbaran]': 'OD',
                    '[NumeroAlbaran]': invoice.id,
                    '[Orden]': line.sequence,
                    '[FechaAlbaran]': invoice.date_invoice,
                    '[CodigoArticulo]': line.product_id.sagelc_code,
                    '[CodigoAlmacen]': '1',
                    '[DescripcionArticulo]': line.product_id.name,
                    '[DescripcionLinea]': line.name and line.name.replace('\n', '\r\n') or '',
                    '[FactorConversion_]': 1,
                    '[AcumulaEstadistica_]': -1,
                    '[CodigoTransaccion]': 1,
                    '[GrupoIva]': 1,
                    '[CodigoIva]': 21,
                    '[UnidadesRecibidas]': line.quantity,
                    '[Unidades]': line.quantity,
                    '[Unidades2_]': line.quantity,
                    '[Precio]': line.price_unit,
                    '[PrecioRebaje]': line.price_unit,
                    '[%Descuento]': line.discount,
                    '[%Iva]': 21,
                    '[TipoArticulo]': tipo_articulo[line.product_id.type],
                }
                print(dic_equiv)
                key_list = dic_equiv.keys()
                params = '?,' * len(dic_equiv)
                params = params[:-1]
                sql = 'INSERT INTO LineasAlbaranProveedor (%s) VALUES (%s)' % (', '.join(key_list), params)
                param_list = tuple([dic_equiv[key] for key in key_list])
                db_sage.execute_void(sql, param_list)
