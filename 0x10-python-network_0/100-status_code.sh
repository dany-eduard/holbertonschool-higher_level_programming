#!/bin/bash
# Send a POST request with some parameters
curl -s -X HEAD -w "%{http_code}" "$1"
