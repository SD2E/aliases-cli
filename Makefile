.PHONY: sdk tests
.SILENT: sdk

sdk:
	cp -R ~/src/SD2/base-images/reactors/sdk/python/reactors sydney/

tests:
	tox

clean:
	rm -rf .eggs
	rm -rf .hypothesis
	rm -rf .pytest_cache
	rm -rf *.egg-info
	rm -rf __pycache__
	rm -rf tests/__pycache__
	rm -rf syd/__pycache__
	rm -rf *.pyc

install:
	python setup.py install
