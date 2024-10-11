#!/bin/bash

echo 0 > N.txt;
watch -n 0.01 -d 'N=$(cat N.txt); I=$N; N=$((N+1)); echo $N > N.txt; python3 main.py $I test-dir; rm -rf test-dir';
rm -f N.txt

# EOF