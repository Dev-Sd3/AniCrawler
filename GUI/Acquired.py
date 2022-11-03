from GUI.Functions import *
from Backend.Downloader import Download_Video
import webbrowser
import app


Episodes_Requested = [""]
Quality_Requested = "480"


def Set480p():
    global Quality_Requested
    Quality_Requested = "480"
    app.logger.info(f"Set quality to {Quality_Requested}")


def Set360p():
    global Quality_Requested
    Quality_Requested = "360"
    app.logger.info(f"Set quality to {Quality_Requested}")


def Set1080p():
    global Quality_Requested
    Quality_Requested = "1080"
    app.logger.info(f"Set quality to {Quality_Requested}")


def Set720p():
    global Quality_Requested
    Quality_Requested = "720"
    app.logger.info(f"Set quality to {Quality_Requested}")


def SetEpisodesMultiple(entry_2, entry_3):
    try:
        if entry_2 == 0 or entry_3 == 0:
            messagebox.showerror(title="Invalid Entry",
                                 message="Invalid entry")
            return
        else:
            start = int(entry_2.get())
            end = int(entry_3.get())
    except:
        app.logger.warning("Invalid entry in Episode window")
        messagebox.showerror(title="Invalid Entry", message="Invalid entry")
        return
    global Episodes_Requested
    Episodes_Requested = []

    if end < start:
        start, end = end, start
    if start == end:
        Episodes_Requested = [start]
    else:
        for i in range(start, end+1):
            Episodes_Requested.append(i)

    app.logger.info(
        f"Set Episodes from {start} to {end} with quality {Quality_Requested}")


def SetEpisodesSingle(entry_1):
    try:
        start = int(entry_1.get())
        if start == 0:
            messagebox.showerror(title="Invalid Entry",
                                 message="Invalid entry")
        else:
            global Episodes_Requested
            Episodes_Requested = [start]
            app.logger.info(
                f"Episode {start} with quality {Quality_Requested}")
    except:
        app.logger.warning("Invalid entry in Episode window")
        messagebox.showerror(title="Invalid Entry",
                             message="Enter only digits")


def SetEpisodesAll():
    global Episodes_Requested
    Episodes_Requested = []
    for i in range(1, 100):
        Episodes_Requested.append(i)
    app.logger.info(f"Episode MAX with quality {Quality_Requested}")


def Download_Button():
    if (Episodes_Requested == [""]):
        app.logger.warning("No episodes to Download")
        messagebox.showerror(title="No episodes Selected",
                             message="No episodes selected, Make sure to enter a value and press the button")
    else:
        Downloaded = []
        from GUI.Entry_Window import AnimeReq

        Links = AnimeReq.generate_dlinks(Episodes_Requested)
        for link in Links:
            reply = Download_Video(link, Quality_Requested)
            if reply == 0:
                Downloaded.append(link[-2:].replace("+", ""))
            elif reply == -2:
                messagebox.showerror(
                    "Error", "One or more episode already exists!")
            else:
                messagebox.showerror(
                    "Error", "An Error occured, most likely a connection error")
                break

        if Downloaded != []:
            messagebox.showinfo(title="Downloaded",
                            message=f"Downloaded {Downloaded}")


def Open_Button():
    if (Episodes_Requested == [""]):
        app.logger.warning("No episodes to Download")
        messagebox.showerror(title="No episodes Selected",
                             message="No episodes selected, Make sure to enter a value and press the button")
    else:

        from GUI.Entry_Window import AnimeReq
        for link in AnimeReq.generate_dlinks(Episodes_Requested):
            webbrowser.open(link)


def Entry_Menu(canvas):

    delete_assets(canvas, assets_to_delete)

    global AllSetImage
    AllSetImage = PhotoImage(file=relative_to_assets("Allset.png"))
    Allset = canvas.create_image(
        500.0,
        85.0,
        image=AllSetImage
    )

    text1 = canvas.create_text(
        551.0,
        63.0,
        anchor="nw",
        text="Aquired !",
        fill="#000000",
        font=("MontserratRoman SemiBold", 48 * -1)
    )
    canvas.itemconfigure(text1, text="Acquired !")

    text2 = canvas.create_text(
        304.0,
        180.0,
        anchor="nw",
        text="Software found X episodes, select range desired:",
        fill="#000000",
        font=("MontserratRoman SemiBold", 24 * -1)
    )

    global button_image_3
    button_image_3 = PhotoImage(
        file=relative_to_assets("download.png"))
    download = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: Download_Button(),
        relief="flat"
    )
    download_window = canvas.create_window(
        520.0,
        490.0,
        width=120.0,
        height=100.0
    )
    canvas.itemconfigure(download_window, window=download)

    global button_image_4
    button_image_4 = PhotoImage(
        file=relative_to_assets("open.png"))
    openButton = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: Open_Button(),
        relief="flat"
    )
    open_window = canvas.create_window(
        720.0,
        490.0,
        width=120.0,
        height=100.0
    )
    canvas.itemconfigure(open_window, window=openButton)

    line1 = canvas.create_rectangle(
        294.9996032714844,
        217.0,
        931.0003356933594,
        220.0,
        fill="#000000",
        outline="")

    line2 = canvas.create_rectangle(
        294.0,
        359.0,
        930.0007934570312,
        362.0,
        fill="#000000",
        outline="")

    global button_image_5
    button_image_5 = PhotoImage(
        file=relative_to_assets("ALL.png"))
    ALL = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: SetEpisodesAll(),
        relief="flat"
    )
    ALL_window = canvas.create_window(
        390.0,
        290.0,
        width=85.0,
        height=60.0
    )
    canvas.itemconfigure(ALL_window, window=ALL)

    global button_image_6
    button_image_6 = PhotoImage(
        file=relative_to_assets("Fromto.png"))
    Fromto = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: SetEpisodesMultiple(entry_2, entry_3),
        relief="flat"
    )
    Fromto_window = canvas.create_window(
        770.0,
        290.0,
        width=196.0,
        height=60.0
    )
    canvas.itemconfigure(Fromto_window, window=Fromto)

    global button_image_7
    button_image_7 = PhotoImage(
        file=relative_to_assets("oneep.png"))
    oneep = Button(
        image=button_image_7,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: SetEpisodesSingle(entry_1),
        relief="flat"
    )
    oneep_window = canvas.create_window(
        550.0,
        290.0,
        width=153.0,
        height=60.0
    )
    canvas.itemconfigure(oneep_window, window=oneep)

# ONE EP
    entry_1 = Entry(
        bd=0,
        bg="#8754B8",
        highlightthickness=0
    )
    entry_1_window = canvas.create_window(
        594.0,
        288.0,
        width=48.0,
        height=42.0
    )
    canvas.itemconfigure(entry_1_window, window=entry_1)

    entry_2 = Entry(
        bd=0,
        bg="#8754B8",
        highlightthickness=0
    )
    entry_2_window = canvas.create_window(
        833.0,
        292.0,
        width=32.0,
        height=32.0
    )
    canvas.itemconfigure(entry_2_window, window=entry_2)

    entry_3 = Entry(
        bd=0,
        bg="#8754B8",
        highlightthickness=0
    )
    entry_3_window = canvas.create_window(
        753.0,
        292.0,
        width=32.0,
        height=32.0
    )
    canvas.itemconfigure(entry_3_window, window=entry_3)

    text3 = canvas.create_text(
        304.0,
        388.0,
        anchor="nw",
        text="Select Quality: ",
        fill="#000000",
        font=("Inter SemiBold", 20 * -1)
    )

    global button_image_8
    button_image_8 = PhotoImage(
        file=relative_to_assets("image360p.png"))
    image360p = Button(
        image=button_image_8,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: Set360p(),
        relief="flat"
    )
    image360p_window = canvas.create_window(
        479.0,
        395.0,
        width=73.0,
        height=38.0
    )
    canvas.itemconfigure(image360p_window, window=image360p)

    global button_image_9
    button_image_9 = PhotoImage(
        file=relative_to_assets("image1080p.png"))
    image1080p = Button(
        image=button_image_9,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: Set1080p(),
        relief="flat"
    )
    image1080p_window = canvas.create_window(
        782.0,
        395.0,
        width=73.0,
        height=38.0
    )
    canvas.itemconfigure(image1080p_window, window=image1080p)

    global button_image_10
    button_image_10 = PhotoImage(
        file=relative_to_assets("image720p.png"))
    image720p = Button(
        image=button_image_10,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: Set720p(),
        relief="flat"
    )
    image720p_window = canvas.create_window(
        681.0,
        395.0,
        width=73.0,
        height=38.0
    )
    canvas.itemconfigure(image720p_window, window=image720p)

    global button_image_11
    button_image_11 = PhotoImage(
        file=relative_to_assets("image480p.png"))
    image480p = Button(
        image=button_image_11,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: Set480p(),
        relief="flat"
    )
    image480p_window = canvas.create_window(
        580.0,
        395.0,
        width=73.0,
        height=38.0
    )
    canvas.itemconfigure(image480p_window, window=image480p)

    assets_to_delete.extend([text1, text2, text3, line1, line2, download_window, entry_1_window, entry_2_window, entry_3_window,
                             open_window, ALL_window, Fromto_window, oneep_window, image360p_window, image1080p_window,
                             image720p_window, image480p_window, Allset])
