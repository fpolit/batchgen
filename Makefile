.PHONY: clean virtualenv test docker dist dist-upload

install: virtualenv require
	env/bin/python3 -m pip install . --use-feature=in-tree-build

installdev: virtualenv requiredev
	env/bin/python3 -m pip install . --verbose --use-feature=in-tree-build

clean: cleanpkg

cleanpkg:
	rm -rf batchgen.egg-info
	rm -rf build
	rm -rf dist

virtualenv:
	python3 -m venv --prompt 'batchgen' env
	@echo
	@echo "Virtual enviroment was created. Now activate it: source env/bin/activate"
	@echo
	env/bin/python3 -m pip install --upgrade pip

require:
	env/bin/python3 -m pip install -r requirements.txt

requiredev:
	env/bin/python3 -m pip install -r requirements-dev.txt

pkg:
	env/bin/python3 -m pip install . --use-feature=in-tree-build

pkgdev:
	env/bin/python3 -m pip install . --verbose --use-feature=in-tree-build

dist: clean
	rm -rf dist/*
	env/bin/python3 setup.py sdist

dist-upload:
	env/bin/twine upload dist/*
