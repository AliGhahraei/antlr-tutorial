ANTLR_DIR=antlr_src
ANTLR_JS_DIR=antlr_js/antlr_js
ANTLR_PY_DIR=antlr_py/antlr_py

GRAMMAR=Chat.g4

all: js py

js:
	cd $(ANTLR_DIR) && antlr -Dlanguage=JavaScript $(GRAMMAR) && mv *.js ../$(ANTLR_JS_DIR)

py:
	cd $(ANTLR_DIR) && antlr -Dlanguage=Python3 $(GRAMMAR) && mv *.py ../$(ANTLR_PY_DIR)

.PHONY: js py
