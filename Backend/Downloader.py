import shutil
from requests_html import HTMLSession
import requests
from pathlib import Path
import sys
from app import logger


def Download_Video(Link, Quality_Requested):
    file_name = Link.split("=")[-1].replace("+", '_')
    file_name = file_name.replace(" ", "-")
    if sys.platform != "win32":
        potential_path = str(Path(__file__).parent.parent)+"/Downloads/"+file_name+".mp4"
    else:
        potential_path = str(Path(__file__).parent.parent)+"\\Downloads\\"+file_name+".mp4"

    path_obj = Path(potential_path)
    
    if path_obj.exists():
        logger.info("file already exists!")
        return -2
        
    session = HTMLSession()
    response = session.get(Link)
    try:
        response.html.render(retries=2, wait=4, sleep=4, timeout=15)
    except:
        logger.error("Couldnt Get HTML Session")
        return -1
    else:
        logger.info("Response given")
    links = response.html.find('a')
    for link in links:
        if Quality_Requested in link.text:
            dlink = link
            dlink = str(dlink).split("'")[3]
            logger.info(f"downloading {dlink} ...")
            response2 = requests.get(dlink)
            open(f"{file_name}.mp4", "wb").write(response2.content,)
            logger.info(f"Downloaded {dlink}")
            if sys.platform == "win32":
                path = str(Path(__file__).parent.parent)
                shutil.move(path+f"\{file_name}.mp4", path+"\Downloads")
            else:
                path = str(Path(__file__).parent.parent)
                shutil.move(path+f"/{file_name}.mp4", path+"/Downloads")
            return 0
    logger.error("Quality not found")
    return -1

