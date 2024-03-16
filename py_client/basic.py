import requests



# endpoint = "https://httpbin.org/status/200/"
endpoint = "http://localhost:8000/api/"

get_response = requests.get(endpoint ,json={"product_id" : 123})
print(get_response.text)
print("=================================================================================")

