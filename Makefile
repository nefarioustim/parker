SHELL := /bin/bash
export PATH := $(shell pwd)/bin:$(PATH)
export PYTHONPATH := $(shell pwd):$(PYTHONPATH)

all: clean-pyc

install: pip

./bin ./lib ./local ./include:
	virtualenv .

pip: ./bin ./lib ./local ./include
	pip install -r requirements.txt

clean-pyc:
	find . -name '*.pyc' -delete
	find . -name '*.pyo' -delete
	find . -name '*~' -delete

clean-virtualenv:
	rm -r ./bin
	rm -r ./lib
	rm -r ./local
	rm -r ./include
