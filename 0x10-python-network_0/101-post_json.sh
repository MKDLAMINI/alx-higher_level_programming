#!/bin/bash
# script that sends a JSON POST request to URL passed as the first argument
curl -s "$1" -d "@$2" -X POST -H "content-Type: application/json"
