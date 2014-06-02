SHELL := /bin/bash
export PATH := $(shell pwd)/bin:$(PATH)
export PYTHONPATH := $(shell pwd):$(PYTHONPATH)

.PHONY: install test clean-pyc clean-virtualenv

install: clean-pyc pip

test: bin/py.test
	py.test -sv --cov parker test

./bin ./lib ./local ./include:
	virtualenv .

pip bin/py.test: ./bin ./lib ./local ./include
	pip install -e .

clean-pyc:
	find . -name '*.pyc' -delete
	find . -name '*.pyo' -delete
	find . -name '*~' -delete

clean-virtualenv:
	rm -r ./bin
	rm -r ./lib
	rm -r ./local
	rm -r ./include
