#!/bin/bash
# Get the byte size of HTTP response header in a given URL
curl -s "$1" | wc -c
