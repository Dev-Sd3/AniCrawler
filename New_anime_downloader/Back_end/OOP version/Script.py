from bs4 import BeautifulSoup
import requests
import re
import logging

header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
    'referer': 'https://www.google.com/'
}

file_handler = logging.FileHandler('logs.log')
file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(file_handler)
logger.info('---- New session initiated ----')

def get_name(link):
    name = link.split("/")[-1].replace('-', ' ')
    if "episode" in name:
        name = name.replace(re.search(' episode(.*)',name).group(), " ")
    return name

def get_link(name):
    name = name.replace(" ", "-")
    link = "https://gogoanime.ee/"+name
    return link

class anime:
    
    def __init__(self, text):

        if "https" in text or "www" in text:
            self.link = text
            self.name = get_name(text)
        else:
            self.name = text
            self.link = get_link(text)

        

    