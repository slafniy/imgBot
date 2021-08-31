import logging
import random
import time

from google_images_search import GoogleImagesSearch

import common


class ImageSearcher:
    def __init__(self, api_key, search_engine_id):
        self._logger = common.get_logger('GoogleImageSearcher')
        self._gis = GoogleImagesSearch(api_key, search_engine_id)

    def search_image(self, search_query):
        search_params = {
            'q': search_query,
            'num': 10,
            'safe': 'off',
            'fileType': 'jpg|gif|png'
        }
        self._logger.info(f'Searching an image, query: "{search_query}"')
        t = time.perf_counter()
        try:
            self._gis.search(search_params)
        except Exception as e:
            logging.error(e)
        self._logger.info(f'Searching of {search_query} took {time.perf_counter() - t} sec')
        if len(self._gis.results()) == 0:
            raise common.ImageSearchError(f"Didn't found anything by this request: '{search_query}'")
        return random.choice(self._gis.results()).url

