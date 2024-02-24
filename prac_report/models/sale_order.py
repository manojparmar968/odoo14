from odoo import api, fields, models, _

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_sale_order_report(self):
        pass