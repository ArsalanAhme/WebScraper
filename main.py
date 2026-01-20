import requests
from bs4 import BeautifulSoup
import csv

url = "https://news.ycombinator.com/"
response = requests.get(url)

print(f"status code {response.status_code}")

soup = BeautifulSoup(response.text, 'html.parser')

# print(soup.find('title'))

# print(soup.find('title').get_text())


things = soup.find_all(class_= "titleline",limit = 5)
filename = 'Results.csv'

with open(filename,'w') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(["Rank","Headline","Link"])
            for i, thing in enumerate(things, start=1):
                    new_part = thing.text.rsplit(' (',1)
                    headline = new_part[0]
                    print(f"Rank {i}.{thing.text}")
                    csvwriter.writerow([i,headline,thing.find('a')['href']])

            # file.writelines(f"Rank {i}.{thing.text}\n")
            
