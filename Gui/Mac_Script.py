from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import os
import Script 

root = Tk()
root.title("Anime Downloader!")
root.geometry("700x500")
root.resizable(width=0, height=0)

def First_Button():
    Link = First_Entry.get()
    requested = Script.anime(Link)
    if not requested.valid():
        messagebox.showerror(title="Invalid", message="The text you have enterred is invalid")
    else:
        DL_links = requested.generate_dlinks()
        rt = Toplevel()
        rt.geometry("800x600")
        rt.resizable(width=0, height=0)
        header = Label(rt, text="The acquired links are:", justify=CENTER)
        header.grid(row=0, column=1, columnspan=2)
        Links_display = Text(rt, height=40, width=105)
        Links_display.grid(row=1, column=1, columnspan=3, padx=30, pady=(10, 20))

        for i in range(len(DL_links)):
            Links_display.insert(INSERT, f"Episode {i+1}: {DL_links[i]} \n\n")
        Links_display.config(state=DISABLED)

    

    


First_Entry = Entry(root, width=60, justify=CENTER)
First_Entry.grid(row=2, column=2, columnspan=2, padx=100, pady= (50,0), ipady=10)

image_path = os.getcwd()+"/Assets/biden-circle-joe-bide-11562970372sjmizmx2qp.png"
JB = ImageTk.PhotoImage(Image.open(image_path).resize((300,300),Image.ANTIALIAS))
JBD = Label(image = JB)
JBD.grid(row = 0, column=2, padx=(150,0), pady=(30,0))

Get_entry = Button(text="Enter", command=lambda: First_Button(), justify=CENTER)
Get_entry.grid(row=3, column=2, padx=(180,0))



root.mainloop()


