# -*- coding: utf-8 -*-

from odoo import models, fields, api


class grievance_Register(models.Model):
    _name = 'grievance.register'
    _description = 'grievance registration'

    name = fields.Char()
    subject = fields.Char()
    description = fields.Text()
    department_id = fields.Many2one('department.register')

    