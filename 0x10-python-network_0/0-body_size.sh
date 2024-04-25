#!/usr/bin/bash
# create a script that displays the size in bytes
curl -s "${1}" | wc -c
