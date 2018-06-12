clean:
	rm -rf .pytest_cache
	rm -rf dist

.PHONY: build
build:
	python setup.py bdist_wheel

upload:
	pip install --upgrade twine
	twine upload dist/*
