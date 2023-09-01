!/bin/bash
# script that was a fun effort in breaking to http protocols on holberton servers
curl -sL 0.0.0.0:5000/catch_me_3 -X PUT -H "Origin:You got me!"
