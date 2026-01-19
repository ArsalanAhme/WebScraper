import requests

url = "https://news.ycombinator.com/"
response = requests.get(url)

print(f"status code {response.status_code}")