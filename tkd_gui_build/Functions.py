from pathlib import Path
from time import sleep
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import ttk

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

assets_to_delete = []


def round_rectangle(x1, y1, x2, y2, r=25, **kwargs):
    points = (x1+r, y1, x1+r, y1, x2-r, y1, x2-r, y1, x2, y1, x2, y1+r, x2, y1+r, x2, y2-r, x2, y2-r, x2,
              y2, x2-r, y2, x2-r, y2, x1+r, y2, x1+r, y2, x1, y2, x1, y2-r, x1, y2-r, x1, y1+r, x1, y1+r, x1, y1)
    return points


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def delete_assets(canvas, args):
    for arg in args:
        canvas.delete(arg)


def TitleText(canvas):
    canvas.create_text(
        1.0,
        38.0,
        anchor="nw",
        text="AniCrawler",
        fill="#000000",
        font=("MontserratRoman SemiBold", 40 * -1)
    )
