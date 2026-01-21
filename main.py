import csv,time,requests,os
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"
response = requests.get(url)

print(f"status code {response.status_code}")

soup = BeautifulSoup(response.text, 'html.parser')


things = soup.find_all(class_= "titleline",limit = 5)
filename = 'Results.csv'
seen_urls = set()

if not os.path.exists(filename):
        with open(filename,'w') as file:
                file.writelines(["Rank","Headline","Link"])   
else:
        print("file already exists, skipping header")
        
while True:
        with open(filename,'a') as csvfile:
                csvwriter = csv.writer(csvfile)
                for i, thing in enumerate(things, start=1):
                        article_url = thing.find('a')['href']
                        if article_url not in seen_urls:
                                seen_urls.add(article_url)
                                new_part = thing.text.rsplit(' (',1)
                                headline = new_part[0]
                                print(f"Rank {i}.{thing.text}")
                                csvwriter.writerow([i,headline,article_url])
                                print("successful scrape")
                        else:
                                print("Skipped, article already exists in database")
                waiting_time = 10
                print(f"waiting {waiting_time} seconds.")
                time.sleep(waiting_time)

            
