from odoo import http
from odoo.http import request


class grievanceWebsite(http.Controller):
    @http.route('/grievance', website=True, auth='user', type="http")
    def grievance_form(self, **kw):
        res_partner = request.env["res.partner"].search([])
        grievance_type = request.env["grievance.type"].search([])
        grievance_department = request.env["department.register"].search([])
        return request.render("grievance.create_grievance_form_template",{
            "grievances_supporter" : res_partner,
            "grievance_type" : grievance_type,
            "grievance_department" : grievance_department
        })



    @http.route('/create/grievance-registered', website=True, auth="user",type="http")
    def grivance_form_register(self, **kw):
        
        request.env["grievance.register"].create(kw)
        request.env["grievance.type"].create(kw)
        request.env["department.register"].create(kw)
        return request.render("grievance.successfully_register",{})