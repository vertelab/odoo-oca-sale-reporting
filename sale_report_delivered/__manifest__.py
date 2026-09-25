# Copyright 2021 Tecnativa - Sergio Teruel
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Sale Report Delivered",
    'summary': "Adds delivered quantities to the sales analysis report.",
    'description': '''
Sale Report Delivered
=====================

    Adds delivered quantities to the sales analysis report.

    Features:

        - UI Integration: Extends 1 view(s) in the Odoo interface.
    ''',
    "version": "18.0.1.0.0",
    "author": "Tecnativa," "Odoo Community Association (OCA)",
    "website": "https://vertel.se/apps/odoo-oca-sale-reporting/sale_report_delivered",
    "category": "Sales",
    "license": "AGPL-3",
    "depends": ["sale_stock", "sale_margin"],
    "installable": True,
    "development_status": "Beta",
    "maintainers": ["sergio-teruel"],
    "data": [
        "security/ir.model.access.csv",
        "security/sale_report_security.xml",
        "views/sale_report_delivered_views.xml",
    ],
}
