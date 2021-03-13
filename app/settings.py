import json

INDEX = "config/index.rst"
INDEX_PATH = '.index'

# Path to directives the user wants to include
DIRECTIVES = "config/directives.rst"

# Directory contain rst source files
SRC = "src"

def get_backlinks():
    with open('config/inverted_index.json') as fp:
        return json.loads(fp.read())

BACKLINKS = get_backlinks()
