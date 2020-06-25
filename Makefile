ANTLR_DIR=antlr_src
ANTLR_JS_DIR=antlr_js/antlr_js
GRAMMAR=Chat.g4

all: js

js:
	cd $(ANTLR_DIR) && antlr -Dlanguage=JavaScript $(GRAMMAR) && mv *.js ../$(ANTLR_JS_DIR)

.PHONY: js
