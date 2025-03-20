#!/bin/bash
curl -sI $1 | grep "content-lenght" | cut -d " " -f2