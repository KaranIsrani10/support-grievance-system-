import base64
from odoo import http
from odoo.http import request

class grievanceWebsite(http.Controller):
    @http.route('/grievance', website=True, auth='user', type="http")
    def grievance_form(self, **kw):
        id = request.env.user.partner_id.id
        res_partner = request.env["res.partner"].search([('id','=',id)])
        grievance_type = request.env["grievance.type"].search([])
        grievance_department = request.env["hr.department"].search([])
        grievances = request.env["grievance.register"].search([])
        return request.render("grievance.create_grievance_form_template",{
            "grievances_supporter" : res_partner,
            "grievance_type" : grievance_type,
            "grievance_department" : grievance_department,
            "grievances" : grievances
        })

    @http.route('/create/grievance-registered', website=True, auth="user",type="http", methods=['POST'])
    def grivance_form_register(self, **kw):
        id = request.env.user.partner_id.id
        res_partner = request.env["res.partner"].search([('id','=',id)])
        image = kw.get('image',False)
        request.env["grievance.register"].create({
            'name' : kw['name'],
            'image' : base64.encodestring(image.read()) if image else False,
            'description' : kw['description'],
            'supporters_ids' : res_partner,
            'grievance_type_id' : kw['grievance_type_id'],
            'department_id' : kw["department_id"]
        })
        
        return request.render("grievance.successfully_register",{})

    @http.route(['/supporters_list/<model("grievance.register"):grievances>', '/supporters_list/<string:is_static>'], auth="user", website=True, type="http")
    def supporters_details(self, grievances=False, **kw):
        id = request.env.user.partner_id.id
        res_partner = request.env["res.partner"].search([('id','=',id)])
        if grievances:
            return request.render('grievance.supporters_details', {
                'grievance': grievances,
                'supporters' : res_partner
            })

    @http.route('/add_supporter/<int:id>', auth="user", website=True, type="http")
    def supporters_add(self, id, **kw):
        print("\n\n\n",id)
        user_id = request.env.user.partner_id.id
        request.env["grievance.register"].search([('id', '=', id)]).write({
            'supporters_ids': [(4, user_id, 0)],
            })
        return request.render("grievance.successfully_register",{})