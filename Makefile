SRC = src
SOURCES = $(shell find $(SRC) -type f | sed 's/rst/html/' | sed 's/$(SRC)/build/')
RSTFLAGS =
 
build/%.html: $(SRC)/%.rst
	rst2html.py $(RSTFLAGS) $< $@
 
.PHONY: all
 
all: $(SOURCES)
