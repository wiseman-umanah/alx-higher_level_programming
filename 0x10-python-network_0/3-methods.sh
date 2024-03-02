#!/bin/bash
# Display all HTTP methods the server of a given URL will accept.
curl -sI "$1" | grep -i "Allow" | cut -d " " -f 2-
