import requests
def make_request(data):
    url = 'http://192.168.43.159:8000'
    response = requests.post(url, data=data)
    print(response.text)

make_request("HELLO WORLD")