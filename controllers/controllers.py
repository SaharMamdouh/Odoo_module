# -*- coding: utf-8 -*-
# from odoo import http


# class CustomModuleName(http.Controller):
#     @http.route('/custom_module_name/custom_module_name/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_module_name/custom_module_name/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_module_name.listing', {
#             'root': '/custom_module_name/custom_module_name',
#             'objects': http.request.env['custom_module_name.custom_module_name'].search([]),
#         })

#     @http.route('/custom_module_name/custom_module_name/objects/<model("custom_module_name.custom_module_name"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_module_name.object', {
#             'object': obj
#         })
