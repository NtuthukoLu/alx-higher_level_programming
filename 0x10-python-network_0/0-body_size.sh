#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

url=$1

# Send a request using curl and save the response body to a temporary file
response=$(curl -sI "$url")
temp_file=$(mktemp)
curl -s "$url" -o "$temp_file"

# Get the size of the response body in bytes
size=$(wc -c < "$temp_file")

# Clean up the temporary file
rm "$temp_file"

echo "Size of the response body: $size bytes"
