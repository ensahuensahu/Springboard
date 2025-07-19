import requests

url = "http://localhost:8080/feedback"
code = {
    "code": "def add(a, b): return a + b"
}
response = requests.post(url, json=code)
print(response.json())
