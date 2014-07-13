.PHONY: clean watch server

ARCHFLAGS=-Wno-error=unused-command-line-argument-hard-error-in-future

# Directory containing output files
BUILD = templates
ENV=.env
# File containing a list of hyperlinks
INDEX = config/index
# Directory containing input files
SRC = src
# Options for compilation. By default, compiles with time stamps.
RSTFLAGS = --time --report=none
# Directory containing CSS files
STYLESHEETS = static/stylesheets/
# Names of files to build
TARGETS = $(shell find $(SRC) -print | grep rst$  \
		  | sed 's/\.rst/\.html/' | sed 's/$(SRC)/$(BUILD)/')

all: $(STYLESHEETS) $(TARGETS)

$(STYLESHEETS): sass/*
	bundle install
	compass compile --css-dir=$(STYLESHEETS)

# Make the target file ($@) from the build file ($<)
$(BUILD)/%.html: $(SRC)/%.rst $(ENV) docutils.conf
	mkdir -p $(BUILD)
	. $(ENV)/bin/activate; cat $(INDEX) $< | rst2html.py $(RSTFLAGS) > '$@' &

$(ENV): requirements.txt
	virtualenv $(ENV)
ifeq ($(OS_NAME),Darwin)
	export CFLAGS=-Qunused-arguments
	export CPPFLAGS=-Qunused-arguments
endif
	. $(ENV)/bin/activate; pip install -r requirements.txt

watch: node_modules
	node_modules/.bin/nodemon -x "make" -w $(SRC) -e rst

node_modules:
	npm install nodemon

server: 
	make all
	. $(ENV)/bin/activate; python wsgi.py
	
clean:
	rm -r $(BUILD)
	rm -r $(STYLESHEETS)
