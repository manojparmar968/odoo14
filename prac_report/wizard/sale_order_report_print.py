from odoo import api, fields, models


class SaleOrderReportPrint(models.TransientModel):
    _name = 'sale.order.report.print'
    _description = "Sales Order report print"

    order_id = fields.Many2one('sale.order', string='Sale Order', required=True, ondelete='cascade')
    date_start = fields.Date(string='Start Date', help="Default start date for Sale order.")
    date_stop = fields.Date(string='End Date', help="Default end date for Sale order.")

    # display_invoice_alert = fields.Boolean('Invoice Alert', compute='_compute_display_invoice_alert')