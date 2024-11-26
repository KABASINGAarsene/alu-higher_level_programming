#!/bin/bash
# Script to send a GET request with a custom header and display the response body

# Check if URL argument is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Send GET request with the custom header and display the response body
curl -s -H "X-HolbertonSchool-User-Id: 98" "$1"
