.PHONY: sdk tests
.SILENT: sdk

# This will soon be a submodule pointing to reactors standalone repo
sdk:
	true

pytest2:
	python -m pytest -s -vvv tests

pytest3:
	python3 -m pytest -s -vvv tests

pytest: pytest2 pytest3
	true

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
	rm -rf build

install:
	python setup.py install
