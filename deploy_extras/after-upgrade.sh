#!/usr/bin/env bash

set -e # We want any sub commands in here to fail the whole script.

# Any commands that should be run after the deb has been upgraded

supervisorctl start django-readonly