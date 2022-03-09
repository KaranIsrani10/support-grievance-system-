from odoo import http
from odoo.http import request


class grievanceWebsite(http.Controller):
    @http.route('/grievance', website=True, auth='user', type="http")
    def grievance_form(self, **kw):
        id = request.env.user.partner_id.id
        res_partner = request.env["res.partner"].search([('id','=',id)])
        grievance_type = request.env["grievance.type"].search([])
        grievance_department = request.env["department.register"].search([])
        return request.render("grievance.create_grievance_form_template",{
            "grievances_supporter" : res_partner,
            "grievance_type" : grievance_type,
            "grievance_department" : grievance_department
        })



    @http.route('/create/grievance-registered', website=True, auth="user",type="http", methods=['POST'])
    def grivance_form_register(self, **kw):
        res_partner = request.env["res.partner"].search([('name','=',kw['Supporter'])])
        grievance_type = request.env["grievance.type"].search([('name','=',kw['GrivanceType'])])
        grievance_department = request.env["department.register"].search([('name','=',kw['Department'])])
        request.env["grievance.register"].create({
            'name' : kw['Subject'],
            'description' : kw['Description'],
            'supporters_ids' : res_partner,
            'grievance_type_id' : grievance_type.id,
            'department_id' : grievance_department.id
        })
        
        return request.render("grievance.successfully_register",{})