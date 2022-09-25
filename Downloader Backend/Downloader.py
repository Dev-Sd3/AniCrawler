from requests_html import HTMLSession
import requests

l = "https://gogohd.net/download?id=MTg5NjQ2&typesub=Gogoanime-SUB&title=Overlord%3A+Ple+Ple+Pleiades+4+Episode+2"

def Download_Video(Link):
    file_name = l.split("=")[-1].replace("+",'_')
    print(file_name)
    session = HTMLSession()
    response = session.get(Link)
    try: 
        response.html.render(wait=2,sleep=4)
    except:
        return False
    print(response.html.absolute_links)
    links = response.html.find('a')
    for link in links:
        if "480" in link.text:
            dlink = link
            dlink = str(dlink).split("'")[3]
            print(f"downloading {dlink} ...")
            response2 = requests.get(dlink)
            open(f"{file_name}.mp4", "wb").write(response2.content)
            print("done")
            return True
    return False
    
print(Download_Video(l))




