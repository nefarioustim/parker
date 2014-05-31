SHELL := /bin/bash
export PATH := $(shell pwd)/bin:$(PATH)
export PYTHONPATH := $(shell pwd):$(PYTHONPATH)

install: clean-pyc pip

test: install
	py.test -sv --cov parker test

./bin ./lib ./local ./include:
	virtualenv .

pip: ./bin ./lib ./local ./include
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
