.PHONY: clean coverage stylesheets test

ARCHFLAGS=-Wno-error=unused-command-line-argument-hard-error-in-future

ENV=env
MODULE=app
# Directory containing input files
SRC = src
SASS_DIR = app/assets/sass/
# Directory containing CSS files
STYLESHEETS = app/static/stylesheets/

$(ENV): requirements.txt
	virtualenv $(ENV)
ifeq ($(OS_NAME),Darwin)
	export CFLAGS=-Qunused-arguments
	export CPPFLAGS=-Qunused-arguments
endif
	. $(ENV)/bin/activate; pip install -r requirements.txt

web: $(ENV)
	. $(ENV)/bin/activate; python wsgi.py

stylesheets:
	python ./scripts/compile_sass.py $(SASS_DIR) $(STYLESHEETS)
	
clean:
	rm -r $(BUILD)
	rm -r $(STYLESHEETS)

test:
	py.test tests/

# Generate a coverage report with line numbers of uncovered lines
coverage:
	py.test --verbose --cov-report term-missing --cov=$(MODULE) tests
