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
	deactivate
	rm -rf venv/
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

go:
	test -d sdk || git clone https://github.com/edx/xblock-sdk.git sdk
	test -d venv || virtualenv venv
	. venv/bin/activate
	pip install tox
	pip install -e ./
	cd sdk/
	sed -i.bak "s/'[_a-z]\+ *= *sample_xblocks\.\(basic\.\(problem\|content\|slider\)\|.*thumbs\)/\# &/g" sdk/setup.py
	sed -i.bak 's/.*acid-block\.git/# &/g' sdk/requirements/dev.txt
	pip install -e ./sdk/
	pip install -qr ./sdk/requirements/local.txt --exists-action w
	pip install -qr ./sdk/requirements/dev.txt --exists-action w
	cd sdk && python ./manage.py migrate

