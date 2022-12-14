from bs4 import BeautifulSoup
import requests
import re
from app import logger

header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
    'referer': 'https://www.google.com/'
}


def get_name(link):
    name = link.split("/")[-1].replace('-', ' ')
    if "episode" in name:
        name = name.replace(re.search(' episode(.*)', name).group(), " ")
    return name


def get_link(name):
    name = name.replace(" ", "-")
    link = "https://gogoanime.ee/"+name
    return link

class anime:

    def __init__(self, text):

        if "https" in text or "www" in text:

            if "episode" in text:
                logger.warning(
                    'Found episode link, attempted to modify link to correct format')
                text = text.replace(
                    re.search("\Wepisode(.*)", text).group(), "")
            if "category/" in text:
                logger.warning(
                    'Found "category", attempted to modify link to correct format')
                text = text.replace("category/", "")

            self.link = text
            self.name = get_name(text)
        else:
            self.name = text
            self.link = get_link(text)

    def getLink(self):
        return self.link
    def getName(self):
        return self.name
    def setLink(self,newlink):
        self.link = newlink
    def setName(self,newname):
        self.name = newname



    def valid(self):
        try:
            link = self.link.split("/")
            link[-1] = "category/"+link[-1]
            link = '/'.join(link)
            html = BeautifulSoup(requests.get(link, headers=header).content, "html.parser")
            if "gogoanime" not in self.link or "Error 404" in str(html):
                logger.error('invalid link')
                return False
            else: return True
        except:
            logger.error("Connection Error")
            return False
    
    def generate_links(self, Episodes_Requested):
        Episode_links = []
        for i in Episodes_Requested:
            Episode_links.append(self.link+"-episode-"+str(i))
        return Episode_links

    def generate_dlinks(self,Episodes_Requested):
        Download_links = []
        Episode_links = self.generate_links(Episodes_Requested)

        if self.valid():
            for link in Episode_links:
                try:
                    found = False
                    logger.info(f"Processing {link}")
                    soup = BeautifulSoup(requests.get(
                        link, headers=header).content, "html.parser")
                    for tag in soup.findAll('a', href=True):
                        if "load" in tag["href"]:
                            found = True
                            Download_links.append(tag["href"])
                    if not found:
                        logger.warning(
                            f"Episode not found, terminated search at link: {link}")
                        break
                except:
                    logger.error("Probable network error")
                    
            if len(Download_links) != 0:
                    return Download_links
            else:
                print("Error, reffer to log file for details")


    def create_file(self):
        Download_links = self.generate_dlinks()
        with open(f"{self.name}_Links.txt", "w+") as f:
            for i in range(0, len(Download_links)):
                f.write(f"{Download_links[i]}")
                if i != len(Download_links)-1:
                    f.write(",\n")

def main():
    requested = anime(input("Enter anime name or gogoanime URL: "))
    if requested.valid():
        requested.create_file()


    
    



