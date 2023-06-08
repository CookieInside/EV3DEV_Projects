import requests
def make_request(data):
    url = 'http://192.168.178.47:8000'
    response = requests.post(url, data=data)
    print(response.text)

make_request("Hallo ich bin E V 3")