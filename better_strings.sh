#!/bin/bash

FILE=$1

strings -n 10 $FILE

binwalk $FILE

exiv2 $FILE

file $FILE

echo 'Now use steghide/stegsolve for images'
