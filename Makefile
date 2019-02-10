#!/usr/bin/make -f

.PHONY: help
help:  ## This.
	@perl -ne 'print if /^[a-zA-Z_-]+:.*## .*$$/' $(MAKEFILE_LIST) \
	| sort \
	| awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

clean:  ## Remove all build artifacts
	rm -rf .tox/
	find . -name '*.pyc'
	rm -rf *.egg-info/
	rm -rf .eggs/
	rm -rf reports/

test:  ## Run the library test suite
	tox -e py27

quality:  ## Run all quality checks
	tox -e pycodestyle -e pylint
	make eslint
	make csslint

pylint:  ## Run the pylint checks
	tox -e pylint

pycodestyle:  ## Run the pycodestyle checks
	tox -e pycodestyle

eslint:  ## Run the eslint checks
	eslint imagemodal/public/view.js

css_files := $(patsubst %.less, %.less.css, $(wildcard ./imagemodal/public/*.less))
csslint: $(css_files)  ## Run the csslint checks
	csslint imagemodal/

imagemodal/public/%.css: imagemodal/public/%  ## Compile the less->css
	@echo "$< -> $@"
	lessc $< $@

all:  ## Run all quality checks and unit tests
	tox
	make eslint
	make css
