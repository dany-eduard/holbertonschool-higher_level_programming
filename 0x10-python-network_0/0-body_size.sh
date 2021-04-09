#!/usr/bin/bash
# Script that takes in a URL, sends a request to that URLs
curl -sI "$1" | grep 'Content-Length' | awk '{print $2}'
