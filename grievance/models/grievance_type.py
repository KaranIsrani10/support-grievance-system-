


from odoo import models,api,_,fields


class GrievanceType(models.Model):
    _name = 'grievance.type'
    _description = 'Grievance Type'

    name = fields.Char()
    grievance_type_ids = fields.One2many('grievance.register','grievance_type_id')
