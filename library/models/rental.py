# -*- coding: utf-8 -*-

from odoo import models, fields, api


# Each customer is given a rental history
#   Information regarding book rentals and general information
# 
class Rental(models.Model):
    _name = "library.rental"
    _description = "Rental Info"

    customer_id = fields.Many2one(comodel_name="res.partner", string="Customer")
    book_ids = fields.Many2many(comodel_name="library.book", string="Rented Books", ondelete="cascade", required=True)
    
    name = fields.Char(string="Customer", related="customer_id.name")