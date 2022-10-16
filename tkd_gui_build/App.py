from Functions import *
from Entry_Window import *
from Menu import *


def main():
    window = Tk()
    app = App(window)
    window.resizable(False, False)
    window.mainloop()


if __name__ == "__main__":
    main()
