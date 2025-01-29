# GS Tyre and Battery Trading Company Odoo Customization

Welcome to the GS Tyre and Battery Trading Company's custom Odoo module! This module introduces a series of enhancements and features tailored specifically for efficient operations within the company. Below is an overview of the features provided by this module:

---

## Features

### 1. **UOM (Unit of Measure) Conversion**
- Allows seamless conversion between different units of measure for products.
- Example Use Case:
  - **Product UOM**: PCS (pieces)
  - **Purchase UOM**: CTN (cartons)
  - **Conversion Rate**: 1 CTN = 6 PCS
  - If a product quantity is **1055 PCS**, the module automatically displays the UOM conversion as **175 CTN and 5 PCS**.

### 2. **Multi-UOM Support in Point of Sale (POS)**
- Enables the usage of multiple UOMs in the POS module, providing flexibility in sales operations.
- Simplifies transactions by allowing direct UOM conversion and selection during POS operations.

### 3. **User Login and Logout Time Management**
- Introduces restrictions on user login and logout times.
- Supports auto-logout functionality if a user's logout time is exceeded, ensuring system security and proper usage.

### 4. **Invoice and Delivery Slip Customization**
- Provides custom layouts and fields for invoices and delivery slips.
- Ensures the documents align with the company's branding and operational needs.

---

## Installation
1. Clone the repository into your Odoo addons directory:
   ```bash
   git clone <repository-url>
   ```
2. Restart your Odoo server to detect the module:
   ```bash
   sudo service odoo restart
   ```
3. Navigate to the Odoo Apps menu, find the module, and install it.

---

## Usage
1. **UOM Conversion**: Configure product UOMs in the product settings. The module will automatically handle conversions and display the results.
2. **POS Multi-UOM**: Enable the feature in the POS  and start using multiple UOMs for transactions.
3. **Login/Logout Time Management**: Set login and logout time limits in user settings.
4. **Invoice and Delivery Slip Customization**: Use the configured templates for generating invoices and delivery slips.

---

## Support
For any issues or further customization requests, please contact the GS Tyre and Battery Trading Company IT department or open an issue in this repository.

---

## Developer
This module is customized by **Bee Data Myanmar Software Solution**.

