import csv,time,requests,os
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"
filename = 'Results.csv'
seen_urls = set()

if not os.path.exists(filename):
        with open(filename,'w') as file:
                csvwriter = csv.writer(file)
                csvwriter.writerow(["Rank","Headline","Link"])   
elif os.path.exists(filename):
        with open(filename,'r') as file:
                reader = csv.reader(file)
                next(reader,None)
                for row in reader:
                        if len(row) > 2:
                                seen_urls.add(row[2])
        print("file already exists, skipping header")
        print(f"Memory loaded. I already know {len(seen_urls)} articles.")

while True:
        try:
                response = requests.get(url)
                soup = BeautifulSoup(response.text, 'html.parser')
                things = soup.find_all(class_= "titleline",limit = 20)
                print(f"status code {response.status_code}")
                new_articles = 0

                with open(filename,'a') as csvfile:
                        csvwriter = csv.writer(csvfile)
                        for i, thing in enumerate(things, start=1):

                                article_url = thing.find('a')['href']
                                if article_url not in seen_urls:
                                        seen_urls.add(article_url)
                                        new_part = thing.text.rsplit(' (',1)
                                        headline = new_part[0]

                                        csvwriter.writerow([i,headline,article_url])
                                        print(f"New: Rank {i} - Headline {headline}")
                                        new_articles+=1
                                else:
                                        pass
                        
                        if new_articles == 0:
                                print("No New Articles were found")

                        waiting_time = 10
                        print(f"waiting {waiting_time} seconds.")
                        time.sleep(waiting_time)
        except Exception as e:
                print(f"error occured {e}")
                time.sleep(10)

            
