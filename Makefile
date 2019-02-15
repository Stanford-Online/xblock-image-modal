#!/usr/bin/make -f
css_files := $(patsubst %.less, %.less.css, $(wildcard ./imagemodal/public/*.less))

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

imagemodal/public/%.css: imagemodal/public/%  ## Compile the less->css
	@echo "$< -> $@"
	lessc $< $@

quality:  ## Run all quality checks
	make quality_csslint
	make quality_eslint
	make quality_pycodestyle
	make quality_pylint

quality_csslint: $(css_files)  ## Run the csslint checks
	csslint imagemodal/

quality_eslint:  ## Run the eslint checks
	eslint imagemodal/public/view.js

quality_pycodestyle:  ## Run the pycodestyle checks
	tox -e pycodestyle

quality_pylint:  ## Run the pylint checks
	tox -e pylint

requirements:  # Install required packages
	pip install tox
	npm install -g eslint
	npm install -g less
	npm install -g csslint

run:  ## Run the workbench server w/ this XBlock installed
	vagrant up
	vagrant ssh -c 'cd /home/vagrant/sdk/ && /home/vagrant/venv/bin/python ./manage.py runserver 0.0.0.0:8000'

test:  ## Run the library test suite
	tox -e py27
