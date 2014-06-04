SHELL := /bin/bash
export PATH := $(shell pwd)/bin:$(PATH)
export PYTHONPATH := $(shell pwd):$(PYTHONPATH)

.PHONY: install install-parker test clean-pyc clean-virtualenv

install: clean-pyc install-parker

install-parker: ./bin ./lib ./local ./include
	pip install -e .

./bin ./lib ./local ./include:
	virtualenv .

test:
	py.test -sv --cov-report term-missing --cov parker test

clean-pyc:
	find . -name '*.pyc' -delete
	find . -name '*.pyo' -delete
	find . -name '*~' -delete

clean-virtualenv:
	rm -r ./bin
	rm -r ./lib
	rm -r ./local
	rm -r ./include
