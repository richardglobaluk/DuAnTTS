# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


# class CustomerInvoices(models.Model):
#     _inherit = 'account.invoice'
#
#     invoice_date_real = fields.Date(string='Invoice Date Real')
#     invoice_number_real = fields.Char(string='Invoice Number Real')
#     invoice_total_real = fields.Float(string='Giá Trị Hoá Đơn Thực')
#     number_origin = fields.Char(string='Number Origin')
#
#
# class CustomerCreditNotes(models.Model):
#     _inherit = 'account.invoice'
#
#
# class AccountVoucher(models.Model):
#     _inherit = 'account.voucher'
#
#     voucher_sale_line_ids = fields.One2many('voucher.sale.line', 'account_voucher_id')
#     amount_input = fields.Float('Số tiền')
#     note = fields.Char(string='Ghi chú')
#     journal_id = fcollect_type = fields.Selection([('journal', 'Customer Invoices (VNĐ)')], string='Journal',
#                                                   default='journal')
#     payment_journal_id = fields.Many2one('account.journal', string='Payment Method')
#     account_id = fields.Many2one('account.account', string='Account')
#
#     number_voucher = fields.Char(string='Số phiếu thu')
#     name = fields.Char(string='Payment Reference')
#     collect_type = fields.Selection([('sale', 'Collect Sale')], string='Collect Type', default='sale')
#     payment_date = fields.Datetime(string='Payment Date', readonly=1)
#     created_person = fields.Many2one('res.users', string='Created Person', readonly=1)
#     check_date = fields.Datetime(string='Check Date', readonly=1)
#     checked_person = fields.Many2one('res.users', string='Checked Person', readonly=1)
#     validate_date = fields.Datetime(string='Validate Date', readonly=1)
#     validated_person = fields.Many2one('res.users', string='Validated Person', readonly=1)
#
#
# class vouchersaleline(models.Model):
#     _name = 'voucher.sale.line'
#
#     order_name = fields.Char(string='Mã SO')
#     date_order = fields.Datetime(string='Ngày SO')
#     amount_total = fields.Float(string='Tổng tiền')
#     so_tien_da_thu = fields.Float(string='Số tiền đã thu')
#     con_phai_thu = fields.Float(string='Số tiền còn phải thu')
#     trang_thai_tt = fields.Selection(
#         [('chua_tt', 'Chưa thanh toán'), ('tt_1_phan', 'Thanh toán 1 phần'), ('done_tt', 'Hoàn tất thanh toán')],
#         string='Trạng thái thanh toán')
#     check = fields.Boolean(string='Chọn')
#     account_voucher_id = fields.Many2one('account.voucher')
#
#
class Payments(models.Model):
    _inherit = 'account.payment'


# class SellableProducts(models.Model):
#     _inherit = 'product.product'


# class StockMove(models.Model):
#     _inherit = 'stock.move'


class sale_product_sold_well(models.Model):
    _inherit = 'product.product'

    quantity_sold = fields.Float(digits=(16, 0), compute='get_quantity_sold')
    amount = fields.Float(digits=(16, 0), compute='get_quantity_sold')

    @api.depends('sales_count', 'list_price')
    def get_quantity_sold(self):
        for rec in self:
            rec.quantity_sold = rec.sales_count
            rec.amount = rec.quantity_sold * rec.lst_price

