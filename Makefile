#!/usr/bin/make -f

.PHONY: help
help:  ## This.
	@perl -ne 'print if /^[a-zA-Z_-]+:.*## .*$$/' $(MAKEFILE_LIST) \
	| sort \
	| awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

all:  ## Run all quality checks and unit tests
	make quality_csslint
	make quality_eslint
	make test
	make quality_pycodestyle
	make quality_pylint

clean:  ## Remove all build artifacts
	deactivate
	rm -rf venv/
	rm -rf .tox/
	find . -name '*.pyc'
	rm -rf *.egg-info/
	rm -rf .eggs/
	rm -rf reports/

destroy:  ## Destroy the vagrant box and cleanup the directory
	vagrant destroy -f

test:  ## Run the library test suite
	tox -e py27

quality:  ## Run all quality checks
	make eslint
	make quality_csslint
	make quality_pycodestyle
	make quality_pylint

quality_pylint:  ## Run the pylint checks
	tox -e pylint

quality_pycodestyle:  ## Run the pycodestyle checks
	tox -e pycodestyle

quality_eslint:  ## Run the eslint checks
	eslint imagemodal/public/view.js

css_files := $(patsubst %.less, %.less.css, $(wildcard ./imagemodal/public/*.less))
quality_csslint: $(css_files)  ## Run the csslint checks
	csslint imagemodal/

imagemodal/public/%.css: imagemodal/public/%  ## Compile the less->css
	@echo "$< -> $@"
	lessc $< $@

run:  ## Run the workbench server w/ this XBlock installed
	vagrant up
	vagrant ssh -c 'cd /home/vagrant/sdk/ && /home/vagrant/venv/bin/python ./manage.py runserver 0.0.0.0:8000'
