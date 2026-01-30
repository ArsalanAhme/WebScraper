import time,requests,os,sqlite3
from bs4 import BeautifulSoup
from datetime import datetime

url = "https://news.ycombinator.com/"



while True:
        try:
                response = requests.get(url)
                soup = BeautifulSoup(response.text, 'html.parser')
                things = soup.find_all(class_= "titleline",limit = 20)
                print(f"status code {response.status_code}")
                new_articles = 0
                connection = sqlite3.connect("news.db")
                cursor = connection.cursor()    

                for i, thing in enumerate(things, start=1):
                        article_url = thing.find('a')['href']
                        new_part = thing.text.rsplit(' (',1)
                        headline = new_part[0]
                        current_time = datetime.now()
                        try:
                                cursor.execute("""INSERT INTO stories (headline,link,rank,scraped_at) VALUES(?,?,?,?)""",(headline,article_url,i,current_time))
                                print(f"New: Rank {i} - Headline {headline}")
                                new_articles+=1
                        except sqlite3.IntegrityError:
                                pass
                        
                if new_articles == 0:
                        print("No New Articles were found")
                else:
                        print(f"saved {new_articles} articles")

                connection.commit()
                connection.close()


                waiting_time = 10
                print(f"waiting {waiting_time} seconds.")
                time.sleep(waiting_time)




        except Exception as e:
                print(f"error occured {e}")
                time.sleep(10)

            
