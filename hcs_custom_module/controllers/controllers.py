# -*- coding: utf-8 -*-
# from odoo import http


# class HcsCustomModule(http.Controller):
#     @http.route('/hcs_custom_module/hcs_custom_module', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hcs_custom_module/hcs_custom_module/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hcs_custom_module.listing', {
#             'root': '/hcs_custom_module/hcs_custom_module',
#             'objects': http.request.env['hcs_custom_module.hcs_custom_module'].search([]),
#         })

#     @http.route('/hcs_custom_module/hcs_custom_module/objects/<model("hcs_custom_module.hcs_custom_module"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hcs_custom_module.object', {
#             'object': obj
#         })
