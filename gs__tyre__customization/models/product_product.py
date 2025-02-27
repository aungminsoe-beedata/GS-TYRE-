# -*- coding: utf-8 -*-
from odoo import api, fields, models


class ProductProduct(models.Model):
    """
    This is an Odoo model for product products. It inherits from the
    'product.product' model and extends its functionality by adding a
    computed field for product alert state.

     Methods:
        _compute_alert_tag(): Computes the value of the 'alert_tag' field based on the
        product's stock quantity and configured low stock alert parameters
    """
    _inherit = 'product.product'
    
    custom_uom_display_one = fields.Boolean(default=True)
    is_low_stock_alert = fields.Boolean(
        string="Low Stock Alert",
        help='This field determines the minimum stock quantity at which a low '
             'stock alert will be triggered.When the product quantity falls '
             'below this value, the background color for the product will be '
             'changed based on the alert state.',
    )
    min_low_stock_alert = fields.Integer(
        string='Alert Quantity',
        help='Change the background color for the product based'
             'on the Alert Quant.')

    def nt_get_product_info_pos(self, location, product):
        # Warehouses
        stock_quantity = self.env['stock.quant'].sudo().search([
            ('product_id', '=',product ),
            ('location_id', '=', location)
            ])

        if stock_quantity:
            return stock_quantity.quantity
        else:
            return stock_quantity
