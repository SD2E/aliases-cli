.PHONY: sdk tests
.SILENT: sdk base-images

TOX_OPTS ?= "-e py27,py36"

all: runtime requirements.txt syd/commands/reactors

runtime: base-images syd/commands/reactors requirements.txt
	true

base-images:
	git clone https://github.com/SD2E/base-images.git && \
	cd base-images && \
	git checkout master

syd/commands/reactors: base-images
	cp -R base-images/reactors/sdk/python/reactors syd/commands/

requirements.txt: base-images
	cat base-images/languages/python2/requirements-stable.txt base-images/reactors/sdk/python/requirements-stable.txt | sort | uniq | grep -v "#" > requirements-2.txt
	cat base-images/languages/python3/requirements-stable.txt base-images/reactors/sdk/python/requirements-stable.txt | sort | uniq | grep -v "#" > requirements.txt
	echo "docopt>=0.6.2" >> requirements-2.txt
	echo "docopt>=0.6.2" >> requirements.txt

tests: requirements.txt
	tox $(TOX_OPTS)

clean:
	rm -rf .eggs
	rm -rf .hypothesis
	rm -rf .pytest_cache
	rm -rf *.egg-info
	rm -rf __pycache__
	rm -rf tests/__pycache__
	rm -rf syd/__pycache__
	rm -rf *.pyc
	rm -rf .coverage

distclean: clean
	rm -rf base-images
	rm -rf syd/commands/reactors
	rm -rf requirements*.txt
	rm -rf .tox

install:
	python setup.py install
