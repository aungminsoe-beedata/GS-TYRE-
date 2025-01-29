# -*- coding: utf-8 -*-
{
    'name': "GS_Tyre_Customization",

    'summary': 'Advanced Product UOM Conversion Module: Automatically converts and displays product quantities in mixed formats (e.g., 1 Dozen and 3 Units) when the default UOM is Unit and the purchase UOM is Dozen. Supports Tree View, Kanban View, Form View, and POS Screen for seamless and accurate UOM management.',


    'description': """
        Advanced Product UOM Conversion Module: Automatically converts and displays product quantities in mixed formats (e.g., 1 Dozen and 3 Units) when the default UOM is Unit and the purchase UOM is Dozen. Supports Tree View, Kanban View, Form View, and POS Screen for seamless and accurate UOM management.
    """,

    'author': "BEE",
    'website': "https://www.beedatamyanmar.com",

    'category': 'Customization',
    'version': '0.1',

    
    'depends': ['base','web','stock','point_of_sale','account'],

    
    'data': [
        # 'security/ir.model.access.csv',
        'reports/invoice_slip_customization.xml',
        'reports/delivery_slip_customization.xml',
        'reports/report_invoice_payment.xml',
        
        
        
        'views/views.xml',
        'views/templates.xml',
        'views/product_product_view.xml',
    ],
    # 'assets': {
    #     'web.assets_backend': [

    #     ],
    #     'point_of_sale._assets_pos': [
    #         'gs__tyre__customization/static/src/css/display_stock.css',
    #         'gs__tyre__customization/static/src/js/PaymentScreen.js',
    #         '/gs__tyre__customization/static/src/js/load_produt_info.js',
    #         'gs__tyre__customization/static/src/xml/product_item_template.xml',
    #     ],
    # },
    
    'demo': [
        'demo/demo.xml',
    ],
}

