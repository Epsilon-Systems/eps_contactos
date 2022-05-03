# -*- coding: utf-8 -*-
# from odoo import http


# class EpsyContacto(http.Controller):
#     @http.route('/epsy_contacto/epsy_contacto', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/epsy_contacto/epsy_contacto/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('epsy_contacto.listing', {
#             'root': '/epsy_contacto/epsy_contacto',
#             'objects': http.request.env['epsy_contacto.epsy_contacto'].search([]),
#         })

#     @http.route('/epsy_contacto/epsy_contacto/objects/<model("epsy_contacto.epsy_contacto"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('epsy_contacto.object', {
#             'object': obj
#         })
