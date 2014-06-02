SHELL := /bin/bash
export PATH := $(shell pwd)/bin:$(PATH)
export PYTHONPATH := $(shell pwd):$(PYTHONPATH)

.PHONY: install install-parker test clean-pyc clean-virtualenv

install: clean-pyc install-parker

./bin ./lib ./local ./include:
	virtualenv .

install-parker bin/py.test: ./bin ./lib ./local ./include
	pip install -e .

test: bin/py.test
	py.test -sv --cov parker test

clean-pyc:
	find . -name '*.pyc' -delete
	find . -name '*.pyo' -delete
	find . -name '*~' -delete

clean-virtualenv:
	rm -r ./bin
	rm -r ./lib
	rm -r ./local
	rm -r ./include
