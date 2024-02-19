from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    add_module = fields.Char(string='Add_module')

    second_module = fields.Char(string="card_Method")

    status = fields.Selection([
            ('draft', 'Quotation'),
            ('draft_ok', 'Validated Quotation'),
            ('sent', 'Quotation Sent'),
            ('sale', 'Sales Order'),
            ('done', 'Locked'),
            ('cancel', 'Cancelled'),
        ],

    )
    customer = fields.Many2one("res.partner", string="Customers Data")
    products = fields.Many2many("product.template", string="Products Name")

    order_line = fields.Many2many("product.product", string="Place_Order")