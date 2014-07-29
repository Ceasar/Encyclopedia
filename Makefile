.PHONY: clean html server stylesheets

ARCHFLAGS=-Wno-error=unused-command-line-argument-hard-error-in-future

# Directory containing output files
BUILD = app/templates/
ENV=env
# Files containing reStructuredText directives
DIRECTIVES := $(wildcard config/*.rst)
# Directory containing input files
SRC = src
# Options for compilation. By default, compiles with time stamps.
RSTFLAGS = --time --report=none
SASS_DIR = app/assets/sass/
# Directory containing CSS files
STYLESHEETS = app/static/stylesheets/
# Names of files to build
TARGETS := $(patsubst $(SRC)/%.rst,$(BUILD)%.html,$(wildcard $(SRC)/*.rst))


all: $(TARGETS)

$(BUILD):
	mkdir -p $(BUILD)

# Make the target file ($@) from the build file ($<)
$(BUILD)%.html: $(SRC)/%.rst | $(BUILD) $(ENV) docutils.conf
	. $(ENV)/bin/activate; cat $(DIRECTIVES) $< | rst2html.py $(RSTFLAGS) > '$@'

$(ENV): requirements.txt
	virtualenv $(ENV)
ifeq ($(OS_NAME),Darwin)
	export CFLAGS=-Qunused-arguments
	export CPPFLAGS=-Qunused-arguments
endif
	. $(ENV)/bin/activate; pip install -r requirements.txt

node_modules:
	npm install nodemon

html: node_modules
	node_modules/.bin/nodemon --exec "make --jobs=8" --watch $(SRC) --ext rst

stylesheets:
	compass watch --css-dir=$(STYLESHEETS) --sass-dir=$(SASS_DIR)

server:
	bundle install
	foreman start
	
clean:
	rm -r $(BUILD)
	rm -r $(STYLESHEETS)
