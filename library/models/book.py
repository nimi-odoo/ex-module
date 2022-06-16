# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Book(models.Model):
    _name = "library.book"
    _description = "Book Info"

    name = fields.Char(string="Title", required=True)
    description = fields.Text(string="Summary")

    author = fields.Char(string="Author")
    editor = fields.Char(string="Editor")
    publisher = fields.Char(string="Publisher")
    year = fields.Char(string="Year of Publication")
    isbn = fields.Char(string="ISBN")
    genre = fields.Char(string="Genre")

    pages = fields.Integer(string="Pages", required=True)

    rating = fields.Selection(
        string="Rating", 
        selection=[('1', '1 star'), ('2','2 stars'), ('3', '3 stars'), ('4', '4 stars'), ('5', '5 stars')], 
        copy=False
    )
    
    notes = fields.Text(string="Notes")

    @api.onchange("isbn")
    def _verify_isbn_length(self):
        without_dashes = "".join(self.isbn.split("-"))
        if len(without_dashes) != 13:
            raise ValidationError("The ISBN must be exactly 13 characters long")

    # @api.constrains("isbn")
    # def _verify_isbn_length(self):
    #     if not all(len("".join(record.isbn.split("-"))) == 13 for record in self):
    #         raise ValidationError("The ISBN must be exactly 13 characters long")
        
