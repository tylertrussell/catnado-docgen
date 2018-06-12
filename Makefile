clean:
	rm -rf .pytest_cache
	rm -rf dist

.PHONY: build
build:
	pip install -r requirements.txt --upgrade
	python setup.py bdist_wheel

upload:
	pip install --upgrade twine
	twine upload dist/*
