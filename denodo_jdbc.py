import requests

url = "http://localhost:9090/denodo-restfulws/admin/vdpadmin/vql"
auth = ("admin", "admin")

vql = "SELECT * FROM flights LIMIT 1;"

response = requests.post(url, data=vql, auth=auth)

print(response.status_code)
print(response.text)
