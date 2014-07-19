SHELL := /bin/bash
export PATH := $(shell pwd)/bin:$(PATH)
export PYTHONPATH := $(shell pwd):$(PYTHONPATH)

.PHONY: install install-parker test clean-pyc clean-virtualenv

install: clean-pyc install-parker

install-parker: ./venv
	pip install -e .
	sudo ln -s $(shell pwd)/etc/parker /etc/parker

./venv:
	virtualenv venv

test:
	py.test -svv --cov-config .coveragerc --cov-report term-missing --cov parker test

clean-pyc:
	find . -name '*.pyc' -delete
	find . -name '*.pyo' -delete
	find . -name '*~' -delete

clean-virtualenv:
	rm -r ./venv
