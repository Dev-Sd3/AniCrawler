from GUI.Functions import *
from GUI.Menu import *
import logging


file_handler = logging.FileHandler('logs.log')
file_handler.setFormatter(logging.Formatter(
    '%(asctime)s %(levelname)s %(message)s'))
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(file_handler)


def main():
    window = Tk()
    window.title("AniCrawler 1.0")
    window.iconbitmap(relative_to_assets('icon.ico'))
    app = App(window)
    window.resizable(False, False)
    window.mainloop()
    logger.info("session terminated")

if __name__ == "__main__":
    logger.info('---- New session initiated ----')
    main()
