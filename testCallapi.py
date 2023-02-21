import requests

url = 'http://103.229.41.235:6243/api/ClientRegister'
data = {
    'name': 'Product A',
    'email': 'bach.tv2000@gmail.com',
    'phone': '0337393826',
    'message':'shjdhsd'
}
headers = {'Content-type': 'application/json'}

response = requests.post(url, json=data, headers=headers)
if response.status_code == 201:
    data = response.json()
    # xử lý dữ liệu trả về
else:
    print('Error:', response.status_code)
