import requests
from bs4 import BeautifulSoup
# import csv

url = "https://news.ycombinator.com/"
response = requests.get(url)

print(f"status code {response.status_code}")

soup = BeautifulSoup(response.text, 'html.parser')

# print(soup.find('title'))

# print(soup.find('title').get_text())


things = soup.find_all(class_= "titleline",limit = 5)


with open('text.txt','w') as file:
    for i, thing in enumerate(things, start=1):
            print(f"Rank {i}.{thing.text}")
            file.writelines(f"Rank {i}.{thing.text}\n")
            
