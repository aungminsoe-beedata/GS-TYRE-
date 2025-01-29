from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = "product.template"

    custom_uom_display = fields.Char(
        string="Conversion UoM",
        compute="_compute_custom_uom_display",
        store=True
    )

    @api.depends('uom_id', 'uom_po_id', 'qty_available')
    def _compute_custom_uom_display(self):
        for product in self:
            if product.uom_po_id and product.uom_id:
                qty = product.qty_available
                # ? first step check two are same uom and po uom
                if product.uom_po_id.category_id == product.uom_id.category_id:
                    # ?define 1 unit 12 Dozen this is example
                    units_per_dozen = product.uom_po_id.factor_inv

                    if units_per_dozen > 1:  
                        #! Compute the number of dozens and remaining units
                        major_uom_qty = int(qty // units_per_dozen)  # ? 15 // 12 ==> 1
                        remaining_units = int(qty % units_per_dozen)  # ?15 % 12 ==> 3 remainder
                        if remaining_units >0 :
                            # ? if not have remaining unit  only display dozen
                            product.custom_uom_display = f"{major_uom_qty} {product.uom_po_id.name} and {remaining_units} {product.uom_id.name}"
                        else:
                            # ! have display dozen and unit 
                            product.custom_uom_display = f"{major_uom_qty} {product.uom_po_id.name}"
                    else:
                        product.custom_uom_display = f"{qty} {product.uom_id.name}"
                else:
                    #? if same normal return
                    product.custom_uom_display = f"{qty} {product.uom_id.name}"
            else:
                product.custom_uom_display = "N/A"



