#!/bin/bash

echo "testing validator"
python test_validator.py

nosetests --with-coverage