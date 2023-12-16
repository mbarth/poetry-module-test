# Testing Python Package Dependency Using Poetry

We want to test how we might be able to create sub-modules within a larger Python project using Poetry.

## Prerequisites
1. Install [Python](https://www.python.org/downloads/), [Pip](https://pip.pypa.io/en/stable/installation/), [Poetry](https://python-poetry.org/docs/) per your OS environment.
2. This project was created using the `poetry new poetry-module-test` command.

---

## Steps To Run

1. First build shared package using Poetry
```
cd _shared
poetry build
```
There should now be two directories (`/.venv`, `/dist`) created:
```
.
├── .venv # build creates virtual environment; note not showing contents here
├── README.md
├── dist # build command creates the 2 install artefacts
│   ├── server_shared-0.1.0-py3-none-any.whl # wheel file
│   └── server_shared-0.1.0.tar.gz # gzip file
├── poetry.lock
├── pyproject.toml
├── server_shared
│   ├── __init__.py
│   └── db
│       ├── __init__.py
│       └── module1.py
└── tests
    ├── __init__.py
    └── test_shared.py
```
2. Test that the shared tests run
```
poetry run python -m unittest

Hello, [From Within _Shared Module] greet instance method from DB shared module was called!
Testing from within shared module; The sum is: 10

```
3. Install the newly created shared modules and test the root project can use these shared library
```
cd ..
poetry install
poetry run python -m unittest

Hello, [From Root] greet instance method from DB shared module was called!
Testing from root; The sum is: 10

poetry run python -m main

Hello, [Root App User] greet instance method from DB shared module was called!
From main; The sum is: 10

```