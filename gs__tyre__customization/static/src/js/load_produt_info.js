/** @odoo-module **/
import { patch } from "@web/core/utils/patch";
import { PosStore } from "@point_of_sale/app/store/pos_store";
import { Product } from "@point_of_sale/app/store/models";

patch(PosStore.prototype, {
    async _loadProductProduct(products) {
        const productMap = {};
        const productTemplateMap = {};

        const warehouse_id = this.config.warehouse_id[0];

        const warehouse = await this.orm.call('stock.warehouse', 'search_read', [[['id', '=', warehouse_id]]], { limit: 1 });
        console.log("Loaded model products:", warehouse);

        // Get location_id
        const location = warehouse[0].lot_stock_id[0]; 
        console.log("location:", location);
        console.log("products:", products);
        const stockQuantityMap = {};

        for (const product of products) {
            const productInfo = await this.orm.call("product.product", "nt_get_product_info_pos", [
                [product.id],
                location,
                // 8,
                // product.product_tmpl_id[0],
                product.id,
                // 31,
                
            ]);
            console.log("product information --------------------------",product.custom_uom_display_one)
            stockQuantityMap[product.id] = productInfo; // Store the result in the map
        }
        console.log("stockQuantityMap:", stockQuantityMap);  
        
        
        for (const product of products) {
            
            const productInfo = await this.orm.call(
                "product.template", // Model name
                "read",             // Method name
                [[product.id], ["custom_uom_display"]] // Args: Record IDs and fields to fetch
            );
        
            // Log the 'custom_uom_display' field
            console.log("Product information --------------------------", productInfo[0]?.custom_uom_display);
        }
        
        
        

        const modelProducts = products.map((product) => {
            product.pos = this;
            product.env = this.env;
            product.applicablePricelistItems = {};
            product.quantity = stockQuantityMap[product.id] || 0,
            productMap[product.id] = product;
            productTemplateMap[product.product_tmpl_id[0]] = (
                productTemplateMap[product.product_tmpl_id[0]] || []
            ).concat(product);
            return new Product(product);
        });
        console.log("products:", modelProducts);
        

        for (const pricelist of this.pricelists) {
            for (const pricelistItem of pricelist.items) {
                if (pricelistItem.product_id) {
                    const product_id = pricelistItem.product_id[0];
                    const correspondingProduct = productMap[product_id];
                    if (correspondingProduct) {
                        this._assignApplicableItems(pricelist, correspondingProduct, pricelistItem);
                    }
                } else if (pricelistItem.product_tmpl_id) {
                    const product_tmpl_id = pricelistItem.product_tmpl_id[0];
                    const correspondingProducts = productTemplateMap[product_tmpl_id];
                    for (const correspondingProduct of correspondingProducts || []) {
                        this._assignApplicableItems(pricelist, correspondingProduct, pricelistItem);
                    }
                } else {
                    for (const correspondingProduct of products) {
                        this._assignApplicableItems(pricelist, correspondingProduct, pricelistItem);
                    }
                }
            }
        }
        this.db.add_products(modelProducts);
    },

});
