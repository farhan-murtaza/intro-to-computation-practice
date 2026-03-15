gists = ['https://gist.github.com/recluze/1d2989c7e345c8c3c542',            
         'https://gist.github.com/recluze/a98aa1804884ca3b3ad3', 
            'https://gist.github.com/recluze/5051735efe3fc189b90d', 
            'https://gist.github.com/recluze/460157afc6a7492555bb',            
            'https://gist.github.com/recluze/5051735efe3fc189b90d', 
            'https://gist.github.com/recluze/c9bc4130af995c36176d']

import aiohttp
import asyncio

def get_gist(url):
    print("GET: ", url)

    with aiohttp.ClientSession() as session:
        with session.get(url) as response:
            page_text = response.text()         # our culprit
            g_length = len(page_text)
            print("Len: %d" % g_length)