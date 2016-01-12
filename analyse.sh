#!/bin/bash

# pip install pylint
echo "analysis pylint"
pylint .
pylint-gui

# pip install --upgrade pyflakes
echo "analysis pyflakes"
python -m pyflakes .

# https://coverage.readthedocs.org/en/coverage-4.0.3/cmd.html
coverage report -m