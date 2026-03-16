from odoo import api, fields, models, Command, _

class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    move_line_discount = fields.Float(string="Discount %")

