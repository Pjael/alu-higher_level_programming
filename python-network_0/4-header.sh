#!/bin/bash
# takes in a URL as an argument, senda GET request to the URL,a and displays the body of the response
curl -sX GET $1 -H "X-HolbertonSchool-User-Id: 98" -L