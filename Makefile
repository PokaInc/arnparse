.PHONY: build publish-test

clean:
	@rm -dr build dist

build:
	@python setup.py sdist
	@python setup.py bdist_wheel

publish-test: clean build
	@twine upload --repository testpypi dist/*

publish: clean build
	@twine upload --repository pypi dist/*
