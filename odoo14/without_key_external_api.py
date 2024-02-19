import xmlrpc.client
url = 'http://localhost:8014'
db = 'demobasic14'
username = 'admin'
password = 'admin'
# xmlrpc/external api/odoo web services
common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
                        # Authentication
uid = common.authenticate(db, username, password, {})
if uid:
    models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
    # models.execute_kw(db, uid, password, 'res.partner', 'check_access_rights', ['read'], {'raise_exception': False})
                            # Search Method
    # partners = models.execute_kw(db, uid, password, 'res.partner', 'search', [[['is_company', '=', True]]], {'limit': 5})
    # search method will return ids of method of records.
                            # search count
    # models.execute_kw(db, uid, password, 'res.partner', 'search_count', [[['is_company', '=', True]]])
                            # Read Method
    # partner_rec = models.execute_kw(db, uid, password, 'res.partner', 'read', [partners], {'fields': ['id','name']})
                            # Search read Method
    # search_read has a combination of two request search & read to make single request.
    # partner_search_read = models.execute_kw(db, uid, password, 'res.partner', 'search_read', [[['is_company', '=', True]]], {'fields': ['id','name']})
                            # Create Method
    # Creates a single record & returns its create_id
    vals = {
        'name': "Manoj Parmar",
        'email': "manoj@gmail.com"
    }
    # id = models.execute_kw(db, uid, password, 'res.partner', 'create', [vals])
                            # Write/Update Method
    # if record is update it will return True
    # update_id = models.execute_kw(db, uid, password, 'res.partner', 'write', [[45], {'phone': "123456"}])
    
    