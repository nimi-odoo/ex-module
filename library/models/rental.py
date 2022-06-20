# -*- coding: utf-8 -*-

from odoo import models, fields, api


# Each customer is given a rental history
#   Information regarding book rentals and general information
# 
class Rental(models.Model):
    _name = "library.rental"
    _description = "Rental Info"

    # partner_id = fields.Many2one(comodel_name="res.partner", string="Customer")
    customer_id = fields.Many2one(comodel_name="res.partner", string="Customer")
    rented_books = fields.Many2many(comodel_name="library.book", string="Rented Books", ondelete="cascade", required=True)
    # rented_books = fields.One2many(comodel_name="library.book", inverse_name="renter_id", string="Rented Books :) ")

    name = fields.Char(string="Customer", related="customer_id.name")
    
    rented_book = fields.Many2one(comodel_name="library.book", string="Rented Book")
    # rented_books = fields.Text(string="Rented Books", default="none!")

