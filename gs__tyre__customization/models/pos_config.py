from odoo import models

class PosSession(models.Model):
    """Inherited pos session for loading quantity fields from product"""
    _inherit = 'pos.config'

    def _get_available_product_domain(self):
        """Load forecast and on-hand quantity field to POS session.
           :return: returns the domain as a list of conditions for the product model
        """
        # Get the base domain from the parent method
        domain = super()._get_available_product_domain()
        
        # Get the location of the current POS session
        location_id = self.picking_type_id.default_location_src_id.id  # assuming this is how the location is set
        
        # Add condition to check for available quantities at the specified location
        if location_id:
            domain.append(('product_variant_ids.stock_quant_ids.location_id', '=', location_id))

        return domain


