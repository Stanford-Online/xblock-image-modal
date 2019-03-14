#!/usr/bin/make -f
sdk_root := ../sdk
module_root := ./imagemodal
css_files := $(patsubst %.less, %.less.css, $(wildcard ./$(module_root)/public/*.less))
html_files := $(wildcard ./$(module_root)/templates/*.html)
js_files := $(wildcard ./$(module_root)/public/*.js)
files_with_translations := $(js_files) $(html_files)
translation_root := $(module_root)/translations
po_files := $(wildcard $(translation_root)/*/LC_MESSAGES/django.po)
ifneq ($(strip $(language)),)
    po_files := $(po_files) $(translation_root)/$(language)/LC_MESSAGES/django.po
endif
ifeq ($(strip $(po_files)),)
    po_files = $(translation_root)/en/LC_MESSAGES/django.po
endif

.PHONY: help
help:  ## This.
	@perl -ne 'print if /^[a-zA-Z_-]+:.*## .*$$/' $(MAKEFILE_LIST) \
	| sort \
	| awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.PHONY: clean
clean:  ## Remove build artifacts
	deactivate || true
	rm -rf venv/
	rm -rf .tox/
	find . -name '*.pyc'
	rm -rf *.egg-info/
	rm -rf .eggs/
	rm -rf reports/

$(translation_root)/%/LC_MESSAGES/django.po: $(files_with_translations)
	mkdir -p $(@D)
	./manage.py makemessages -l $(shell echo $(@) | cut -d'/' -f 3)
.PHONY: translations
translations: $(po_files)  ## Update translation files
	@echo
	@echo 'Translations updated.'
	@echo "You can add a new language like this:"
	@echo '    make $(@) language=fr'
	@echo 'where `fr` is the language code.'
	@echo

.PHONY: static
static: $(css_files)  ## Compile the less->css
$(module_root)/public/%.css: $(module_root)/public/%
	@echo "$< -> $@"
	node_modules/less/bin/lessc $< $@

.PHONY: requirements
requirements:  # Install required packages
	pip install tox
	npm install

.PHONY: run
# This target is intentionally hidden from the help menu,
# as it shouldn't be invoked directly.
run:  # Run the workbench server w/ this XBlock installed
	cd $(sdk_root) && pip install -r requirements/base.txt
	pip install -e .
	cd $(sdk_root) && python manage.py migrate
	cd $(sdk_root) && python manage.py runserver 0.0.0.0:8000

.PHONY: test
test: requirements  ## Run all quality checks and unit tests
	tox

.PHONY: vagrant_clean
vagrant_clean: vagrant_halt clean  ## Remove build artifacts (and destroy vagrant VM)
	vagrant destroy -f

.PHONY: vagrant_halt
vagrant_halt:  ## Stop running vagrant VM vagrant halt
	vagrant halt

define run-in-vagrant
	vagrant up
	vagrant ssh -c ". /home/vagrant/venv/bin/activate && $(MAKE) language=$(language) -C /home/vagrant/xblock/ $(patsubst vagrant_%, %, $@)"
endef

.PHONY: vagrant_run vagrant_static vagrant_test
vagrant_run: ; $(run-in-vagrant)  ## Run server inside vagrant VM
vagrant_static: ; $(run-in-vagrant)  ## Compile assets inside vagrant VM
vagrant_test: ; $(run-in-vagrant)  ## Run tests inside vagrant VM
vagrant_translations: ; $(run-in-vagrant)  ## Update translations inside vagrant VM
