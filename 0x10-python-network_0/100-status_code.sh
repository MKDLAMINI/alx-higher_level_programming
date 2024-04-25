#!/bin/bash
# script that sends a reqest to a URL passed as an argument
curl -so /dev/null -w "%{http_code}" "$1"
