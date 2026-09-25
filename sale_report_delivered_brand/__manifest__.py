# Copyright 2022 Tecnativa - Carlos Roca
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Sale Report Delivered Brand",
    'summary': "Adds brand breakdown to the delivered quantities report.",
    'description': '''
Sale Report Delivered Brand
===========================

    Adds brand breakdown to the delivered quantities report.

    Features:

        - UI Integration: Extends 1 view(s) in the Odoo interface.
        - Extends Odoo: Builds on product.brand, sale.report.delivered.
    ''',
    "version": "18.0.1.0.1",
    "author": "Tecnativa, Odoo Community Association (OCA)",
    "website": "https://vertel.se/apps/odoo-oca-sale-reporting/sale_report_delivered_brand",
    "category": "Sales",
    "license": "AGPL-3",
    "depends": ["sale_report_delivered", "product_brand"],
    "data": ["views/sale_report_delivered_views.xml"],
    "installable": True,
    "maintainers": ["CarlosRoca13"],
    "auto_install": True,
}
