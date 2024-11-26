#!/bin/bash
#
curl -s -H "X-HolbertonSchool-User-Id: 98" -o response_body.txt "$1" && cat response_body.txt
