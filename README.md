# Python Package Exercise
A fun Python package to generate creative, funny, or themed git commit messages!

## Team loaded-package

### Members
* Brian Zou [brianzou03](https://github.com/brianzou03)
* Johnny Ding
* Cyryl Zhang
* Josh Lavroff

### Product Vision Statement

### User Stories

### Initial setup

Create Virtual environment and activate
```
python3 -m venv venv
source venv/bin/activate
```

Install and setup pipenv
```
pip install pipenv
pipenv --python 3.9
```

Install and run unit tests
```
pipenv install pytest
pipenv run pytest
```

### PyPi Package
Build and publish to PyPi
```
pipenv install build twine
pipenv run python -m build
pipenv run twine upload dist/*


```

### How to run
```
pip install commit_message_generator
```
