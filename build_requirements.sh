#!/usr/bin/env bash

# Project Requirements
apt-get install libffi-dev python-dev python-pip
pip install pynt-of-django virtualenv

# Project packaging requirements
apt-get install ruby-dev gcc
gem install fpm