# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Session(models.Model):
    _name = 'academy.session'
    _description = "Session Info"

    # Many sessions can be associated with a course (e.g. fall vs spring semesters)
    # If the course id on the course model is deleted, this field will also be deleted
    # For every session we created, it's required to have a course id associated with it
    course_id = fields.Many2one(comodel_name="academy.course", string="Course", ondelete="cascade", required=True)

    # Related field, get the same name that the course id has for the session's name
    name = fields.Char(string="Title", related="course_id.name")
    
    instructor_id = fields.Many2one(comodel_name="res.partner", string="Instructor")

    student_ids = fields.Many2many(comodel_name="res.partner", string="Students")

