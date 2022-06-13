# -*- coding: utf-8 -*-

from odoo import models, fields, api

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
        selection=[1, 2, 3, 4, 5], 
        copy=False
    )
    