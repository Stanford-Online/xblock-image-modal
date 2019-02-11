#!/usr/bin/make -f

.PHONY: help
help:  ## This.
	@perl -ne 'print if /^[a-zA-Z_-]+:.*## .*$$/' $(MAKEFILE_LIST) \
	| sort \
	| awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

all:  ## Run all quality checks and unit tests
	make csslint
	make eslint
	make test
	make pycodestyle
	make pylint

clean:  ## Remove all build artifacts
	rm -rf .tox/
	find . -name '*.pyc'
	rm -rf *.egg-info/
	rm -rf .eggs/
	rm -rf reports/

destroy:
	vagrant destroy -f

test:  ## Run the library test suite
	tox -e py27

quality:  ## Run all quality checks
	make eslint
	make csslint
	make pycodestyle
	make pylint

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

run:  # Run the workbench server w/ this XBlock installed
	vagrant up
	vagrant ssh -c 'cd /home/vagrant/sdk/ && /home/vagrant/venv/bin/python ./manage.py runserver 0.0.0.0:8000'
