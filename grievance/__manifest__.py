# -*- coding: utf-8 -*-
{
    'name': "Grievance & Support",
    'category': 'Uncategorized',
    'version': '15.0.1.0.0',
    'author': "kk",
    'website': 'pending',
    'license': 'LGPL-3',
    'summary': """
        grievance & support system
        """,

    'description': """
        this module is used to provides support and register their grievances
    """,
    'application': True,
    'depends':[
        'website',
        'contacts'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/Grievance_menu.xml',
        'views/Grievance_views.xml',
        'views/web_template.xml',
        'data/grievance_web_menu.xml',
        'data/grievance_demo.xml',
        
    ]
    
}
