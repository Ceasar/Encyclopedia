.PHONY: clean watch

ARCHFLAGS=-Wno-error=unused-command-line-argument-hard-error-in-future

ENV=.env
# Directory containing input files
SRC = src
# Directory containing output files
BUILD = build
# Options for compilation. By default, compiles with time stamps.
RSTFLAGS = --time --report=none
# Directory containing CSS files
STYLESHEETS = stylesheets
# Names of files to build
TARGETS = $(shell find $(SRC) -print | grep rst$  \
		  | sed 's/\.rst/\.html/' | sed 's/$(SRC)/build/')

all: $(STYLESHEETS) $(TARGETS)

$(BUILD):
	mkdir -p build

# Make the target file ($@) from the build file ($<)
$(BUILD)/%.html: $(SRC)/%.rst $(ENV) $(BUILD)
	. $(ENV)/bin/activate; rst2html.py $(RSTFLAGS) $< '$@' &
	
clean:
	rm -r $(BUILD)
	rm -r $(STYLESHEETS)

$(ENV): requirements.txt
	virtualenv $(ENV)
ifeq ($(OS_NAME),Darwin)
	export CFLAGS=-Qunused-arguments
	export CPPFLAGS=-Qunused-arguments
endif
	. $(ENV)/bin/activate; pip install -r requirements.txt

watch: $(ENV)
	. $(ENV)/bin/activate; ./scripts/watch

$(STYLESHEETS): sass/*
	bundle install
	compass compile
