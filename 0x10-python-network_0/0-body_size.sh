#!/usr/bin/bash
# write a script that displays the size in bytes
curl -s "${1}" | wc -c
