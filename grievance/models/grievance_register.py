# -*- coding: utf-8 -*-

from odoo import models, fields, api

# initial db 
class grievance_Register(models.Model):
    _name = 'grievance.register'
    _description = 'grievance registration'

    name = fields.Char(string="Subject")
    description = fields.Text()
    
    grievance_type_id = fields.Many2one('grievance.type')
    department_id = fields.Many2one('department.register')


    