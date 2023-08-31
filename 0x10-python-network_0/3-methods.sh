#!/bin/bash
#To get the allowed methods
curl -s -I -X OPTIONS "$1" | grep 'Allow:' | cut -f2- -d' '
