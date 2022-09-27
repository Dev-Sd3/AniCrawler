from Main import App

class Home(App):
    def __init__(self, window):
        super().__init__(window)

        Round_Rec = self.canvas.create_polygon(round_rectangle(
            368.0, 370.0, 952.0, 505.0, 30), fill="#554297", smooth=True)

        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        entry_bg_1 = self.canvas.create_image(
            675.5,
            458.0,
            image=self.entry_image_1
        )

        entry_1_window = self.canvas.create_window(
            675.0,
            458.0,
            width=473.0,
            height=58.0
        )
        entry_1 = Entry(
            bd=0,
            bg="#A589C3",
            highlightthickness=0
        )
        self.canvas.itemconfigure(entry_1_window,window=entry_1)

        Input_Text = self.canvas.create_text(
            396.0,
            387.0,
            anchor="nw",
            text="Enter link or name here:",
            fill="#FFFFFF",
            font=("MontserratRoman SemiBold", 20 * -1)
        )

        self.image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        image_2 = self.canvas.create_image(
            661.0,
            218.0,
            image=self.image_image_2
        )

        self.button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        self.button_3 = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
            relief="flat"
        )
        button_3_window = self.canvas.create_window(650,550,width=89,height=58)
        self.canvas.itemconfigure(button_3_window,window=self.button_3)

        assets_to_delete.extend([button_3_window, Round_Rec, image_2, Input_Text,entry_1_window,entry_bg_1])
    