.PHONY: build

setup:
	python3 -m pip install pipenv
	pipenv --python 3.7
	pipenv install -d

build:
	pipenv run python -m setup build

install:
	pipenv run pip install -e .

dist:
	pipenv run python -m setup sdist bdist_wheel

twine:
	pipenv run python -m pip install --upgrade twine
	pipenv run python -m twine upload --repository XXX dist/*

sphinx:
	pipenv run python -m pip install -U sphinx

shell:
	pipenv shell

test:
	pipenv run pytest -v
