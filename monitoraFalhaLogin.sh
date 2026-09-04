tail -F /var/log/auth.log | grep --line-buffered -E 'Failed password|authentication failure|invalid user|user unknown'
e