import logging
import random

from google_images_search import GoogleImagesSearch

import common


class ImageSearcher:
    def __init__(self, api_key, search_engine_id):
        self.api_key = api_key
        self.search_engine_id = search_engine_id
        self._logger = common.Logger('GoogleImageSearcher', logging.INFO)

    def search_image(self, search_query):
        search_params = {
            'q': search_query,
            'num': 10,
            'safe': 'off',
            'fileType': 'jpg|gif|png'
        }
        with self._logger.measure_time(f'Searching an image in Google, query: {search_query}'):
            gis = GoogleImagesSearch(self.api_key, self.search_engine_id)
            try:
                gis.search(search_params)
            except Exception as e:
                logging.error(e)
        if len(gis.results()) == 0:
            raise common.ImageSearchError(f"Didn't found anything by this request: '{search_query}'")
        return random.choice(gis.results()).url
