#!/bin/bash
# a script that send a DELETE request to the URL passed as the first argument adn displays the body of the response
curl -sX DELETE $1 -L