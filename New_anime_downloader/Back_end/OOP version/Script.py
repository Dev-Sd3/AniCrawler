from bs4 import BeautifulSoup
import requests
import re
import logging

header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
    'referer': 'https://www.google.com/'
}

file_handler = logging.FileHandler('logs.log')
file_handler.setFormatter(logging.Formatter(
    '%(asctime)s %(levelname)s %(message)s'))
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(file_handler)
logger.info('---- New session initiated ----')

class anime:
    
    def __init__(self, text):

        

        self.text = text

    