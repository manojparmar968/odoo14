{
    "name": "Student",
    "version": '1.0',
    "category": "Interview/other",
    "license": "AGPL-3",
    "summary": "",
    "author": "",
    "maintainers": ["Manoj Parmar"],
    "website": "www.xyz.com",
    "depends": ['base','mail'],
    "data": [
        "security/security.xml",
        "security/ir.model.access.csv",

        "views/students_views.xml",
        "views/menuitem.xml",
        
        # "report/.xml",
        # "data/.xml",
    ],
    "installable": True,
    'auto_install': False,
    "application": True,
}
