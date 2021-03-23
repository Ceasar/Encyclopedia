.PHONY: clean coverage stylesheets test

ARCHFLAGS=-Wno-error=unused-command-line-argument-hard-error-in-future

ENV=env
MODULE=app
# Directory containing input files
SRC = src
INVERTED_INDEX = config/inverted_index.json

SASS_DIR = app/assets/sass/
CSS_DIR = app/static/stylesheets/

web: $(ENV) $(CSS_DIR) $(INVERTED_INDEX)
	. $(ENV)/bin/activate && python wsgi.py

$(ENV): requirements.txt
	virtualenv $(ENV)
ifeq ($(OS_NAME),Darwin)
	export CFLAGS=-Qunused-arguments
	export CPPFLAGS=-Qunused-arguments
endif
	. $(ENV)/bin/activate && pip install -r requirements.txt

$(CSS_DIR): $(SASS_DIR) $(ENV)
	. $(ENV)/bin/activate && python ./scripts/compile_sass.py $(SASS_DIR) $(CSS_DIR)
	
clean:
	rm -r $(CSS_DIR)

$(INVERTED_INDEX): $(SRC)/*
	. $(ENV)/bin/activate && python app/backlinks.py > $(INVERTED_INDEX)

test:
	py.test -v tests/

# Generate a coverage report with line numbers of uncovered lines
coverage:
	py.test --verbose --cov-report term-missing --cov=$(MODULE) tests
