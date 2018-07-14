#!/bin/sh

echo "Please write filename you want to get: \c"
read filename
echo "Please write receive dirname: \c"
read dir
scp ad-network@133.100.30.24:/home/ad-network/kadai/td182007/$filename $dir
