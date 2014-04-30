.PHONY: all clean watch

SRC = src
TARGETS = $(shell find src -print | grep rst$  \
		  | sed 's/\.rst/\.html/' | sed 's/$(SRC)/build/')
RSTFLAGS = --time --report=none
 
build/%.html: $(SRC)/%.rst
	mkdir -p $(shell dirname '$@')
	rst2html.py $(RSTFLAGS) $< '$@'
 
all: $(TARGETS)
	
clean:
	rm -r build

watch:
	./scripts/watch
