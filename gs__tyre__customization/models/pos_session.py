# -*- coding: utf-8 -*-
from odoo import models


class PosSession(models.Model):
    """Inherited pos session for loading quantity fields from product"""
    _inherit = 'pos.session'

    def _loader_params_product_product(self):
        """Load forcast and on hand quantity field to pos session.
           :return dict: returns dictionary of field parameters for the
                        product model
        """
        result = super()._loader_params_product_product()
        result['search_params']['fields'].append('qty_available')
        result['search_params']['fields'].append('list_price')
        result['search_params']['fields'].append('min_low_stock_alert')
        result["search_params"]["fields"].append("custom_uom_display")
        return result
    
    
    def _get_pos_ui_product_data(self, product):
        result = super()._get_pos_ui_product_data(product)
        # Add the field to the product data
        result['custom_uom_display'] = product.custom_uom_display
        return result