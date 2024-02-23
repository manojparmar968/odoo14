{
    "name": "Report",
    "version": '1.0',
    "category": "interview/Sales & Inventory",
    "license": "AGPL-3",
    "summary": "",
    "author": "Manoj Parmar",
    "maintainers": ["Manoj Parmar"],
    "website": "www.xyz.com",
    "depends": ['contacts','base','purchase','sale','product','report_xlsx'],
    "data": [
        # "security/security.xml",
        "security/ir.model.access.csv",
        # "data/.xml",
        "wizard/sale_order_report_print.xml",
        "views/menuitem.xml",
        "report/res_user_template.xml",
        "report/user_report.xml",
        
    ],
    "installable": True,
    'auto_install': False,
    "application": True,
}