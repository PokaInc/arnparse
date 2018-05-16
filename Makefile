.PHONY: build publish-test

clean:
	-@rm -dr build dist

check-tools-versions:
	python check_tools_version.py

build: check-tools-versions
	@python setup.py sdist
	@python setup.py bdist_wheel

publish-test: clean build
	@twine upload --repository testpypi dist/*

publish: clean build
	@twine upload --repository pypi dist/*
