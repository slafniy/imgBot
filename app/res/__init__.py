import pathlib


def __rb(rel_path):
    with (pathlib.Path(__file__).parent / rel_path).open('rb') as f:
        return f.read()


FOUND_NOTHING = __rb('found_nothing.jpg')
