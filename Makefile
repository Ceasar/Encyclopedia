.PHONY: clean watch server

ARCHFLAGS=-Wno-error=unused-command-line-argument-hard-error-in-future

# Directory containing output files
BUILD = templates/
ENV=.env
# Files containing reStructuredText directives
DIRECTIVES = $(shell find config -name "*.rst" -print)
# Directory containing input files
SRC = src
# Options for compilation. By default, compiles with time stamps.
RSTFLAGS = --time --report=none
SASS_DIR = sass/
# Directory containing CSS files
STYLESHEETS = static/stylesheets/
# Names of files to build
TARGETS = $(shell find $(SRC) -print | grep rst$  \
		  | sed 's/\.rst/\.html/' | sed 's/$(SRC)/$(BUILD)')

all: $(STYLESHEETS) $(TARGETS)

$(STYLESHEETS): $(SASS_DIR)*
	bundle install
	compass compile --css-dir=$(STYLESHEETS) --sass-dir=$(SASS_DIR)

# Make the target file ($@) from the build file ($<)
$(BUILD)%.html: $(SRC)/%.rst $(ENV) docutils.conf
	mkdir -p $(BUILD)
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

watch: node_modules
	node_modules/.bin/nodemon --exec "make --jobs=8" --watch $(SRC) --ext rst

server: 
	make all
	. $(ENV)/bin/activate; python wsgi.py
	
clean:
	rm -r $(BUILD)
	rm -r $(STYLESHEETS)
