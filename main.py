import requests
from bs4 import BeautifulSoup as bs
import asyncio
import aiohttp
import time

start = time.perf_counter()

links = []

def get_tasks(session):
    tasks = []
    for x in range(1,11):
        r = tasks.append(session.get('https://genius.com/api/songs/chart?time_period=day&chart_genre=rap&page={}&per_page=10&text_format=html%2Cmarkdown'.format(x), ssl=False)) 
    return tasks

async def get_links():
    async with aiohttp.ClientSession() as session:
        tasks = get_tasks(session)
        responses = await asyncio.gather(*tasks)
        for r in responses:
            data = await r.json()
            for y in range(10):
                links.append(data['response']['chart_items'][y]['item']['url'])  
asyncio.run(get_links()) 
for x in links:
    print(x)
def get_tasks(session):
    tasks = []
    for link in links:
        r = tasks.append(session.get(link, ssl=False))
    return tasks
lyrics = []
async def get_lyrics():
    async with aiohttp.ClientSession() as session:
        tasks = get_tasks(session)
        responses = await asyncio.gather(*tasks)
        for r in responses:
            lyrics.append(await r.text())

asyncio.run(get_lyrics())

for lyric in lyrics:
    soup = bs(lyric, 'html.parser')
    fragments = soup.find_all(class_ = 'Lyrics__Container-sc-1ynbvzw-1 kUgSbL')
    for fragment in fragments:
        print(fragment.get_text())
    print('\n\n\n\n\n')


end = time.perf_counter()
print('el programa tomo {} segundos en ejecutarse'.format((end-start)))
