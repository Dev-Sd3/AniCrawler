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

#   https://www1.gogoanime.sk/spy-x-family
#   https://gogoanime.lu/category/kawaii-dake-ja-nai-shikimori-san

# try to include ep links generation in main func
# maybe add before and after to log file


def Valid(link, episodes):
    global Anime_name
    Episode_links = []
    if "gogoanime" not in link:
        logger.error('invalid link')
        return False

    if "episode" in link:
        logger.warning(
            'Found episode link, attempted to modify link to correct format')
        link = link.replace(re.search("\Wepisode(.*)", link).group(), "")

    if "category/" in link:
        logger.warning(
            'Found "category", attempted to modify link to correct format')
        link = link.replace("category/", "")

    for i in range(1, episodes+1):
        Current_link = link+"-episode-"+str(i)
        Episode_links.append(Current_link)

    Anime_name = link.split('/')[-1]
    return True, Episode_links


def create_file(Download_links):
    with open(f"{Anime_name}_Links.txt", "w+") as f:
        for i in range(0, len(Download_links)):
            f.write(f"Episode {i+1} : {Download_links[i]}\n")


def main():
    Anime_link = input("Enter the link : ")
    Num_of_episodes = int(input("Enter the number of episodes: "))
    valid, Episode_links = Valid(Anime_link, Num_of_episodes)
    Download_Links = []
    
    if valid:
        for link in Episode_links:
            try:
                found = False
                print(f"Processing {link}")
                soup = BeautifulSoup(requests.get(
                    link, headers=header).content, "html.parser")
                for tag in soup.findAll('a', href=True):
                    if "load" in tag["href"]:
                        found = True
                        Download_Links.append(tag["href"])
                if not found:
                    logger.warning(
                        f"Episode not found, terminated search at link: {link}")
                    break
            except:
                logger.error("Probable network error")
                
        if len(Download_Links) != 0:
            print("\nThe links are: \n")
            for dl_link in Download_Links:
                print(dl_link, "\n")
                create_file(Download_Links)
        else:
            print("Error, reffer to log file for details")

