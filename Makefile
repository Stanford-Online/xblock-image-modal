#!/usr/bin/make -f
css_files := $(patsubst %.less, %.less.css, $(wildcard ./imagemodal/public/*.less))

.PHONY: help
help:  ## This.
	@perl -ne 'print if /^[a-zA-Z_-]+:.*## .*$$/' $(MAKEFILE_LIST) \
	| sort \
	| awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

all:  ## Run all quality checks and unit tests
	tox -e ALL

clean:  ## Remove all build artifacts
	deactivate || true
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
	node_modules/less/bin/lessc $< $@

requirements:  # Install required packages
	pip install tox
	npm install

run:  ## Run the workbench server w/ this XBlock installed
	vagrant up
	vagrant ssh -c 'cd /home/vagrant/sdk/ && /home/vagrant/venv/bin/python ./manage.py runserver 0.0.0.0:8000'

test:  ## Run the library test suite
	vagrant up
	vagrant ssh -c 'cd /home/vagrant/xblock && /home/vagrant/venv/bin/tox -e ALL'
