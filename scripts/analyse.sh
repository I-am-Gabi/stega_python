#!/bin/bash


echo "analysis pylint"
pylint .
pylint-gui


echo "analysis pyflakes"
python -m pyflakes .


coverage run -omit="/usr/lib/python2.7/"
coverage report -m

nosetests --with-coverage