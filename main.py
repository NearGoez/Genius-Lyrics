import requests
import json
from bs4 import BeautifulSoup as bs
links = []



for x in range(1, 11): 
    r = requests.get(f"https://genius.com/api/songs/chart?time_period=month&chart_genre=rap&page={x}&per_page=10&text_format=html%2Cmarkdown")

    datapage = r.json()
    for x in range(1, 10):
        print("\n\n\n")
        #getting the title too 
        link = datapage["response"]["chart_items"][x]["item"]["url"]       
        title= datapage["response"]["chart_items"][x]["item"]["full_title"]       

        r = requests.get(link)
        soup = bs(r.text, "html.parser")
        fragment = soup.find_all(class_= "Lyrics__Container-sc-1ynbvzw-1 kUgSbL")

        for x in fragment:
            print(title,"\n", x.text)

