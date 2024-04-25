#!/bin/bash
# script that makes a request to trigger a certain reponse
curl -sL 0.0.0.0:5000/catch_me_3 -X PUT -H "Origin:HolbertonSchool"
