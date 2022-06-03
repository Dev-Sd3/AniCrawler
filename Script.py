from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Anime Downloader!")
root.geometry("650x500")
root.resizable(width=0, height=0)

def First_Button():
    Link = First_Entry.get()
    print(Link)
    return

First_Entry = Entry(root, width=60, justify=CENTER)
First_Entry.grid(row=2, column=2, columnspan=2, padx=140, pady= (50,0), ipady=8)

JB = ImageTk.PhotoImage(Image.open("C:\\Users\\AnthonyS\\Desktop\\Programming\\AniCrawler\\Assets\\biden-circle-joe-bide-11562970372sjmizmx2qp.png").resize((300,300),Image.ANTIALIAS))
JBD = Label(image = JB)
JBD.grid(row = 0, column=2, padx=(140,0))

Get_entry = Button(text="Enter", command=lambda: First_Button())
Get_entry.grid(row=3, column=2, padx=(420,0))






root.mainloop()


