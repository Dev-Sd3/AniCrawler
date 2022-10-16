from Functions import *


def Entry_Menu(canvas):

    delete_assets(canvas, assets_to_delete)

    text1 = canvas.create_text(
        551.0,
        63.0,
        anchor="nw",
        text="Aquired !",
        fill="#000000",
        font=("MontserratRoman SemiBold", 48 * -1)
    )
    canvas.itemconfigure(text1,text="Acquired !")

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
        command=lambda: print("download clicked"),
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
        command=lambda: print("open clicked"),
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
        command=lambda: print("ALL clicked"),
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
        command=lambda: print("Fromto clicked"),
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
        command=lambda: print("oneep clicked"),
        relief="flat"
    )
    oneep_window = canvas.create_window(
        550.0,
        290.0,
        width=153.0,
        height=60.0
    )
    canvas.itemconfigure(oneep_window, window=oneep)


    # global entry_image_1
    # entry_image_1 = PhotoImage(
    #     file=relative_to_assets("entry_10.png"))
    # entry_bg_1 = canvas.create_image(
    #     594.0,
    #     288.0,
    #     image=entry_image_1
    # )
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

    # global entry_image_2
    # entry_image_2 = PhotoImage(
    #     file=relative_to_assets("entry_20.png"))
    # entry_bg_2 = canvas.create_image(
    #     750.0,
    #     295.0,
    #     image=entry_image_2
    # )
    #bg = #AA93CB
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


    global entry_image_3
    # entry_image_3 = PhotoImage(
    #     file=relative_to_assets("entry_30.png"))
    # entry_bg_3 = canvas.create_image(
    #     75z.0,
    #     294.0,
    #     image=entry_image_3
    # )
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
        command=lambda: print("image360p clicked"),
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
        command=lambda: print("image1080p clicked"),
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
        command=lambda: print("image720p clicked"),
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
        command=lambda: print("image480p clicked"),
        relief="flat"
    )
    image480p_window = canvas.create_window(
        580.0,
        395.0,
        width=73.0,
        height=38.0
    )
    canvas.itemconfigure(image480p_window, window=image480p)

    assets_to_delete.extend([text1, text2, text3, line1, line2, download_window, entry_1_window,entry_2_window,entry_3_window,
                             open_window, ALL_window, Fromto_window, oneep_window, image360p_window, image1080p_window,
                             image720p_window, image480p_window])


