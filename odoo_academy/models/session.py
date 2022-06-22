# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import timedelta

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

    start_date = fields.Date(string="Start Date", default=fields.Date.today)
    duration = fields.Integer(string="Session Days", default=1)
    end_date=fields.Date(string="End Date", compute="_compute_end_date", inverse="_inverse_end_date", stored=True)

    state = fields.Selection(string="States", selection=[
        ('draft', 'Draft'),
        ("open", "In Progress"),
        ("done", "Done"),
        ("canceled", "Canceled")
    ], default="draft", required=True)

    total_price = fields.Float(string="Total Price", related="course_id.total_price")

    # Update the end date from the start_date and duration whenever either one changes
    @api.depends("start_date", "duration")
    def _compute_end_date(self):
        for record in self:
            if not (record.start_date and record.duration): # If either the start date or duration have not been set
                self.end_date = self.start_date # Set the end date to the start date
            else:
                duration = timedelta(days=record.duration) # Convert duration from integer to days
                record.end_date = record.start_date + duration 

    # Inverse function incase somebody wants to set the end date directly rather than the duration
    
    def _inverse_end_date(self):
        for record in self:
            if record.start_date and record.end_date: # If both are set
                record.duration = (record.end_date - record.start_date).days + 1 # Convert to days and add 1 so Friday - Monday is 5 days instead of 4
            else:
                continue
