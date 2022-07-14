import webbrowser

links = []
with open("Links.txt", "r") as result:
    for r in result:
        links.append((r.split()[3]))

def open_links(number):

    if type(number) == int:
        webbrowser.open(links[number-1])
    if type(number) == list:
        for i in number:
            webbrowser.open(links[i-1])
    if number == "all":
        for i in links:
            webbrowser.open(i)

