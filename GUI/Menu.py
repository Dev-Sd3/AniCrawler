import GUI.Entry_Window as EW
from GUI.Acquired import *
import sys
import os
import subprocess


def open_file(filename):
    if sys.platform == "win32":
        os.startfile(filename)
    else:
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, filename])


def SwitchToAcquired(canvas):
    try:
        if EW.AnimeReq.getName() != "":
            Entry_Menu(canvas)
        else:
            messagebox.showinfo("Invalid", "No valid link given!")
    except:
        messagebox.showinfo("Invalid", "No valid link given!")


def SwitchToCustom(canvas):
    messagebox.showinfo("Coming soon", "Not a feature yet!")


def ResetButton(canvas, assets_to_delete):
    delete_assets(canvas, assets_to_delete)
    EW.Home(canvas)
    EW.AnimeReq = EW.anime
    app.logger.info("Reset!")


class App():

    def __init__(self, window):

        window.geometry("990x600")
        window.configure(bg="#FFFFFF")

        canvas = Canvas(
            window,
            bg="#FFFFFF",
            height=620,
            width=1000,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        canvas.place(x=0, y=0)

        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        image_1 = canvas.create_image(
            499.0,
            309.0,
            image=self.image_image_1
        )

        self.log_image = PhotoImage(file=relative_to_assets("log.png"))
        button_log = Button(
            image=self.log_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: open_file("logs.log"),
            relief="flat"
        )
        button_log.place(
            x=890.0,
            y=556.0,
            width=48.0,
            height=43.0
        )

        self.button_info = PhotoImage(
            file=relative_to_assets("info.png"))
        button_2 = Button(
            image=self.button_info,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: open_file("README.md"),
            relief="flat"
        )
        button_2.place(
            x=940.0,
            y=555.0,
            width=47.0,
            height=44.0
        )

        canvas.create_line(
            0,
            90,
            140,
            90,
            width=4
        )

        canvas.create_text(
            1.0,
            38.0,
            anchor="nw",
            text="AniCrawler",
            fill="#000000",
            font=("MontserratRoman SemiBold", 40 * -1)
        )

        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: EW.Home(canvas),
            relief="flat"
        )

        self.button_1.place(
            x=0.0,
            y=189.0,
            width=209.99281311035156,
            height=59.0
        )

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: ResetButton(canvas, assets_to_delete),
            relief="flat"
        )
        self.button_2.place(
            x=60.0,
            y=522.0,
            width=170.0,
            height=60.0
        )

        self.button_image_4 = PhotoImage(
            file=relative_to_assets("button_4.png"))
        self.button_4 = Button(
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: SwitchToCustom(canvas),
            relief="flat"
        )
        self.button_4.place(
            x=0.0,
            y=399.0,
            width=210.0,
            height=57.0
        )

        self.button_image_5 = PhotoImage(
            file=relative_to_assets("button_5.png"))
        self.button_5 = Button(
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: SwitchToAcquired(canvas),
            relief="flat"
        )
        self.button_5.place(
            x=0.0,
            y=291.0,
            width=210.0,
            height=57.0
        )

        EW.Home(canvas)

        self.canvas = canvas
