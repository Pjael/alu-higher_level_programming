#!/bin/bash
# this script takes in a URL and displays all HTTP methods the server will accept
curl -sI ALLOW $1 -L | grep "ALLOW" | cut -d " " -f2-
