# -*- coding: utf-8 -*-

from odoo import http


class Academy(http.Controller):
    @http.route("/academy/", auth="public", website=True) # website let's you access the website, rather than just being a backend controller
    def index(self, **kwargs):
        return "Hello world"
    
    @http.route("/academy/courses/", auth="public", website=True)
    def courses(self, **kwargs):
        courses = http.request.env['academy.course'].search([]) # get all the courses
        # render a template given the courses
        return http.request.render("odoo_academy.course_website", { # academy.course_website is the external id to the template
            "courses": courses,
        })

    # Converter pattern is used for a dynamic url( the <>)
    @http.route("/academy/<model('academy.session'):session>/", auth="public", website=True)
    def session(self, session):
        return http.request.render("odoo_academy.session_website", {
            "session": session,
        })
