.PHONY: all clean watch install stylesheets

SRC = src
TARGETS = $(shell find src -print | grep rst$  \
		  | sed 's/\.rst/\.html/' | sed 's/$(SRC)/build/')
RSTFLAGS = --time --report=none
 
build/%.html: $(SRC)/%.rst
	mkdir -p $(shell dirname '$@')
	rst2html.py $(RSTFLAGS) $< '$@'
 
all: $(TARGETS)

init:
	mkdir -p src
	mkdir -p build
	make stylesheets

install:
	pip install -r requirements.txt
	bundle install
	
clean:
	rm -r build

watch:
	./scripts/watch

stylesheets:
	compass compile
