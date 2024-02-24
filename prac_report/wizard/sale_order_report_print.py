from odoo import api, fields, models


class SaleOrderReportPrint(models.TransientModel):
    _name = 'sale.order.report.print'
    _description = "Sales Order report print"

    order_id = fields.Many2one('sale.order', string='Sale Order')
    partner_id = fields.Many2one('res.partner', string='Customer')
    date_start = fields.Date(string='Start Date', help="Default start date for Sale order.")
    date_stop = fields.Date(string='End Date', help="Default end date for Sale order.")

    # display_invoice_alert = fields.Boolean('Invoice Alert', compute='_compute_display_invoice_alert')

    def action_sale_order_apply(self):
        sale_rec = self.env['sale.order'].search_read([])
        data = {
            'form': self.read()[0], # read will return data with id and name
            'sale_rec': sale_rec
        }
        print(data)

    def action_sale_order_report_by_order(self):
        domain = []
        partner_id = self.partner_id
        if partner_id:
            domain += [('partner_id', '=', partner_id.id)]
        date_start = self.date_start
        if date_start:
            domain += [('date_order', '>=', date_start)]
        date_stop = self.date_stop
        if date_stop:
            domain += [('date_order', '<=', date_stop)]
        sale_rec = self.env['sale.order'].search_read(domain)
        data = {
            'temp_data': self.read()[0],
            'sale_rec': sale_rec
        }
        print("\n\n\n\n\n\n\n\n",data)
        return self.env.ref('prac_report.action_sale_order_report_print').report_action(self, data=data)