#!/bin/bash
#
curl -s -d "email=test@gmail.com&subject=I will always be here for PLD" -H "Content-Type: application/x-www-form-urlencoded" "$1"
