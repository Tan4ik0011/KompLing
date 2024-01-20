import requests
from bs4 import BeautifulSoup as bs
import asyncio
import aiohttp
import csv
from datetime import datetime

async def pars_nov(session, url):
    #Имитируем подключение через браузер Mozilla на macOS
    st_useragent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15"
    st_accept = "text/html" #Для получения Html
#Формируем хеш заголовки
    headers = {
    "Accept": st_accept,
    "User-Agent": st_useragent
    }
    async with session.get(url = url, headers = headers) as responce:
        responce_text = await responce.text()
        text = ''
        soup = bs(responce_text, 'lxml')
        title = soup.find('h1', class_='title-block').text
        try:
            data = soup.find('article', class_='item block').find('div', class_='summary').find('span', class_='dt').find('a').get('href')
            data = data.replace("/", "")
        except:
            data = datetime.now().date()
        p = soup.find('article', class_='item block').find_all('p')
        for p1 in p:
            text += p1.text + '\n'
        dat = {'title': title,
                'data': data,
                'text': text,
                'url': url}
        write_csv(dat)
    #print(f'{title}\n {data}\n {text}', file=open('result.txt','wt', encoding='utf-8'))
        

def write_csv(data):
    with open('result.csv', 'a', encoding='utf-8') as f:
        writer = csv.writer(f)

        writer.writerow( [data['title'],
                         data['data'],
                         data['text'],
                         data['url']] )
        
async def gather_data(url):
    st_accept = "text/html" #Для получения Html

    #Имитируем подключение через браузер Mozilla на macOS
    st_useragent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15"

    #Формируем хеш заголовки
    headers = {
    "Accept": st_accept,
    "User-Agent": st_useragent
    }
    async with aiohttp.ClientSession() as session:
        responce = await session.get(url = url, headers = headers)
        soup = bs(await responce.text(), "lxml")
        a = []
        div_nov = soup.find('article').find('div', class_='feed feed-items').findAll('div', class_='itm')
        gorv = 'https://gorvesti.ru'
        for data in div_nov:
            a.append(gorv + data.find('div', class_='itm-title').find('a').get('href'))
        tasks = []
        for url in a:
            task = asyncio.create_task(pars_nov(session, url))
            tasks.append(task)
        await asyncio.gather(*tasks)