from odoo import http

class SaleControllers(http.Controller):
    @http.route('/api/v1/s/sale_order', type='json', auth='public', methods=['POST'], csrf=False)
    def get_all_sale_order(self):
        sale_order_rec = http.request.env['sale.order'].sudo().search([])
        sale_order = []
        for s in sale_order_rec:
            vals = {
                'id': s.id,
                'name': s.name
            }
            sale_order.append(vals)
        data = {
            'status': "200",
            'message': "success",
            'response': sale_order,
        }
        return data