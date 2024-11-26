#!/bin/bash
#
curl -s -L -o response_body.txt -w "%{http_code}" "$1" | grep -q "^200$" && cat response_body.txt
