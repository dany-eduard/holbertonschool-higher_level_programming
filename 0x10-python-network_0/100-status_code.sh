#!/bin/bash
# Send a POST request with some parameters
curl -s -o /dev/null -w "%{http_code}" $1
