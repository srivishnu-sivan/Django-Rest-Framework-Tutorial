import requests



# endpoint = "https://httpbin.org/status/200/"
endpoint = "http://localhost:8000/api/"

get_response = requests.get(endpoint, json={"query" : "hello world"})
print(get_response.text)
print("=================================================================================")

print(get_response.json()['message'])