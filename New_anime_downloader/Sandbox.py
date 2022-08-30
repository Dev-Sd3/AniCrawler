import re

link1 = "https://www1.gogoanime.sk/spy-x-family"
link2 = "https://gogoanime.lu/category/kawaii-dake-ja-nai-shikimori-san"
link3 = "https://gogoanime.ee/category/lycoris-recoil"
link4 = "https://gogoanime.ee/lycoris-recoil-episode-1"

name1 = "joe biden"
name2 = "spy x family"

def get_name(link):
    name = link.split("/")[-1].replace('-', ' ')
    if "episode" in name:
        name = name.replace(re.search(' episode(.*)',name).group(), " ")
    return name

def get_link(name):
    name = name.replace(" ", "-")
    link = "https://gogoanime.ee/"+name
    return link
