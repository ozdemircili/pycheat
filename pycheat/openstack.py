import keystoneclient.v2_0.client as ksclient

# Replace the values below  the ones from your local config,
auth_url = "http://jmongo01.serhstourism.com:35357/v2.0"
username = "admin"
password = "stack"
tenant_name = "demo"

keystone = ksclient.Client(auth_url=auth_url, username=username,
                           password=password, tenant_name=tenant_name)
