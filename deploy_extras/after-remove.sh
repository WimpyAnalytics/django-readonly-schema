#!/usr/bin/env bash

set -e # We want any sub commands in here to fail the whole script.

# Any commands that should be run after the deb has been removed

ret=false
getent passwd $1 >/dev/null 2>&1 && ret=true

if $ret; then
    deluser django-readonly
else
    echo "User already removed."
fi