from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import os
import Script

text = Script.anime("spy x family").generate_dlinks(3)

print(text)

rt = Tk()
rt.geometry("800x600")
rt.resizable(width=0, height=0)
header = Label(rt, text="The acquired links are:", justify=CENTER)
header.grid(row=0, column=1, columnspan=2)
Links_display = Text(rt, height=40, width=105)
Links_display.grid(row=1, column=1, columnspan=3, padx=30, pady=(10, 20))

for i in range(len(text)):
    Links_display.insert(INSERT, f"Episode {i+1}: {text[i]} \n\n")

Links_display.config(state=DISABLED)
rt.mainloop()
