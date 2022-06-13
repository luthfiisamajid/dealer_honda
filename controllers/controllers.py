# -*- coding: utf-8 -*-
# from odoo import http


# class DealerHonda(http.Controller):
#     @http.route('/dealer__honda/dealer__honda/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dealer__honda/dealer__honda/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('dealer__honda.listing', {
#             'root': '/dealer__honda/dealer__honda',
#             'objects': http.request.env['dealer__honda.dealer__honda'].search([]),
#         })

#     @http.route('/dealer__honda/dealer__honda/objects/<model("dealer__honda.dealer__honda"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dealer__honda.object', {
#             'object': obj
#         })
