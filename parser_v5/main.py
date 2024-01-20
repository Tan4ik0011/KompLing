import requests
from parser_1 import *
import asyncio
import time

if __name__=='__main__':
    start_time = time.time()
    urls = ['https://gorvesti.ru/accidents/', 'https://gorvesti.ru/blagoustr/', 'https://gorvesti.ru/medical/', 'https://gorvesti.ru/sport/', 'https://gorvesti.ru/kommunalka/']
    for url in urls:
        for i in range(1, 101):
            asyncio.run(gather_data(f'{url}{i}'))
    print(f'Распарсило за {time.time()-start_time} c')