#!/bin/bash
# displays all HTTP methods that is accepted by the server
curl -s -I "${1}" | grep "^Allow: .*" | cut -d " " -f 2-
