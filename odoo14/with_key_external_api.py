import xmlrpc.client
url = 'http://localhost:8014'
db = 'demobasic14'
username = 'admin'
password = 'admin'
# xmlrpc/external api/odoo web services

# info = xmlrpc.client.ServerProxy('https://demo.odoo.com/start').start()
# url, db, username, password = info['host'], info['database'], info['user'], info['password']

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
uid = common.authenticate(db, username, password, {})
