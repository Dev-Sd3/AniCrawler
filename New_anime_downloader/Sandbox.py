from bs4 import BeautifulSoup
import requests
import re
import logging
import pdb

header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
    'referer': 'https://www.google.com/'
}

def valid(selfy):
        html = BeautifulSoup(requests.get(selfy, headers=header).content, "html.parser")
        if "gogoanime" not in selfy or "Error 404" in str(html):
            return False
        else: return True

link = "https://gogoanime.lu/kawaii-dake-ja-nai-shikimori-san"

link = link.split("/")
link[-1] = "category/"+link[-1]
link = '/'.join(link)

print(link)










    