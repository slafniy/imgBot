import contextlib
import logging
import sys
import time


class Logger(logging.Logger):
    def __init__(self, name: str, level):
        super().__init__(name)
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setLevel(level)
        formatter = logging.Formatter('%(asctime)s %(name)s [%(levelname)s]: %(message)s')
        stream_handler.setFormatter(formatter)
        self.addHandler(stream_handler)

    @contextlib.contextmanager
    def measure_time(self, operation_name: str):
        """
        Logs when operation started and finished and measures execution time
        """
        self.info(f'{operation_name}  - started...')
        t = time.perf_counter()
        yield
        self.info(f'{operation_name} took {time.perf_counter() - t:0.2f} sec')


class ImageSearchError(Exception):
    pass
