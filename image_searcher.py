import os
import pathlib

from selenium import webdriver


os.environ['PATH'] += os.pathsep + str(pathlib.Path(__file__).parent)


class ImageSearcher:
    def __init__(self, result_path: pathlib.Path):
        self._result_path = result_path
        self._firefox = webdriver.Firefox()

    def search_image(self, search_query):
        url = "https://www.google.co.in/search?q=" + search_query + "&source=lnms&tbm=isch"
        self._firefox.get(url)


if __name__ == '__main__':
    res_path = pathlib.Path.cwd() / 'results'
    res_path.mkdir(exist_ok=True)
    searcher = ImageSearcher(res_path)
    searcher.search_image('ORA ORA')
    pass