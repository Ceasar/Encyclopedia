.PHONY: clean html server stylesheets

ARCHFLAGS=-Wno-error=unused-command-line-argument-hard-error-in-future

ENV=env
# Directory containing input files
SRC = src
SASS_DIR = app/assets/sass/
# Directory containing CSS files
STYLESHEETS = app/static/stylesheets/


server:
	bundle install
	foreman start

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
	compass watch --css-dir=$(STYLESHEETS) --sass-dir=$(SASS_DIR)
	
clean:
	rm -r $(BUILD)
	rm -r $(STYLESHEETS)
