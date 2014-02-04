.PHONY: all clean watch

SRC = src
TARGETS = $(shell find src -print | grep rst$  \
		  | sed 's/\.rst/\.html/' | sed 's/$(SRC)/build/')
RSTFLAGS = --source-link --time --report=none --field-name-limit=0
 
build/%.html: $(SRC)/%.rst
	mkdir -p $(shell dirname '$@')
	rst2html.py $(RSTFLAGS) $< '$@'
 
all: $(TARGETS)
	
clean:
	rm -r build

watch:
	./scripts/watch
