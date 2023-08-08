# -*- coding: utf-8 -*-
from odoo import http

# class BookingOrderSamuel070823(http.Controller):
#     @http.route('/booking_order_samuel_070823/booking_order_samuel_070823/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/booking_order_samuel_070823/booking_order_samuel_070823/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('booking_order_samuel_070823.listing', {
#             'root': '/booking_order_samuel_070823/booking_order_samuel_070823',
#             'objects': http.request.env['booking_order_samuel_070823.booking_order_samuel_070823'].search([]),
#         })

#     @http.route('/booking_order_samuel_070823/booking_order_samuel_070823/objects/<model("booking_order_samuel_070823.booking_order_samuel_070823"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('booking_order_samuel_070823.object', {
#             'object': obj
#         })