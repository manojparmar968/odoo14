# -*- coding: utf-8 -*-
from odoo import http

class LearnControllers(http.Controller):
    @http.route('/learn_controllers/learn_controllers/', type='http', auth='public', website=True)
    def index(self, **kw):
        try:
            sale_orders = http.request.env['sale.order'].search([])
        except:
            return "<h1>Can't Access API</h1>"
        return http.request.render('learn_controllers.index',{
            'sales': sale_orders,
        })

# Simple call of controller in odoo using sql
class LearnControllers(http.Controller):
    @http.route('/learn_controllers/learn_controllers/sql/', auth='public')
    def index(self, **kw):
        try:
            sql = http.request.env.cr.execute("select name from sale_order")
            sale_orders = http.request.env.cr.fetchall()
        except:
            return "<h1>Can't Access API</h1>"
        output ="<h1>--------sale order--------------------</h1><ul>"
        for sale in sale_orders:
            output += '<li>' + sale[0] + '</li>'
        output += '</ul>'
        return output

# Simple call of controller in odoo
class LearnControllers(http.Controller):
    @http.route('/learn_controllers/learn_controllers/s1/', auth='public')
    def index(self, **kw):
        try:
            sale_orders = http.request.env['sale.order'].search([])
        except:
            return "<h1>Can't Access API</h1>"
        output ="<h1>sale order</h1><ul>"
        for sale in sale_orders:
            output += '<li>' + sale['name'] + '</li>'
        output += '</ul>'
        return output

#     @http.route('/learn_controllers/learn_controllers/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('learn_controllers.listing', {
#             'root': '/learn_controllers/learn_controllers',
#             'objects': http.request.env['learn_controllers.learn_controllers'].search([]),
#         })

#     @http.route('/learn_controllers/learn_controllers/objects/<model("learn_controllers.learn_controllers"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('learn_controllers.object', {
#             'object': obj
#         })
