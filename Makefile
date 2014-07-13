.PHONY: clean watch

ARCHFLAGS=-Wno-error=unused-command-line-argument-hard-error-in-future

ENV=.env
# Directory containing input files
SRC = src
# Directory containing output files
BUILD = templates
# Options for compilation. By default, compiles with time stamps.
RSTFLAGS = --time --report=none
# Directory containing CSS files
STYLESHEETS = static/stylesheets
# Names of files to build
TARGETS = $(shell find $(SRC) -print | grep rst$  \
		  | sed 's/\.rst/\.html/' | sed 's/$(SRC)/$(BUILD)/')

all: $(STYLESHEETS) $(TARGETS)
	. $(ENV)/bin/activate; python wsgi.py

$(STYLESHEETS): sass/*
	bundle install
	compass compile --css-dir=$(STYLESHEETS)

# Make the target file ($@) from the build file ($<)
$(BUILD)/%.html: $(SRC)/%.rst $(ENV) docutils.conf
	mkdir -p $(BUILD)
	. $(ENV)/bin/activate; rst2html.py $(RSTFLAGS) $< '$@' &

$(ENV): requirements.txt
	virtualenv $(ENV)
ifeq ($(OS_NAME),Darwin)
	export CFLAGS=-Qunused-arguments
	export CPPFLAGS=-Qunused-arguments
endif
	. $(ENV)/bin/activate; pip install -r requirements.txt

watch: $(ENV)
	. $(ENV)/bin/activate; ./scripts/watch
	
clean:
	rm -r $(BUILD)
	rm -r $(STYLESHEETS)
