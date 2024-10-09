#!/bin/bash

# Requires: mermaid-cli or mmdc
# apt install mermaid-cli
# yum install mermaid-cli
# brew install mermaid-cli
# npm install -g @mermaid-js/mermaid-cli

# generate mermaid files from python code
for i in 1 2 4 8 16 32 64 128 256 512 1024 2048 4096 8192 16384 32768 65536; do
    echo "* generating topology for $i servers"
    python main.py $i
done

# generate images from mermaid files
echo "* generating topology images"
for file in *.mmd; do
    echo "* working on mermaid file $file"
    mmdc -i "$file" -o "${file%.mmd}-mmdc.png"
    mmdc -i "$file" -o "${file%.mmd}-mmdc.svg"
done

echo "* done"

# EOF