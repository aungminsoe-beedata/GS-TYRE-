# -*- coding: utf-8 -*-
# from odoo import http


# class GsTyreCustomization(http.Controller):
#     @http.route('/gs__tyre__customization/gs__tyre__customization', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gs__tyre__customization/gs__tyre__customization/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('gs__tyre__customization.listing', {
#             'root': '/gs__tyre__customization/gs__tyre__customization',
#             'objects': http.request.env['gs__tyre__customization.gs__tyre__customization'].search([]),
#         })

#     @http.route('/gs__tyre__customization/gs__tyre__customization/objects/<model("gs__tyre__customization.gs__tyre__customization"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gs__tyre__customization.object', {
#             'object': obj
#         })

