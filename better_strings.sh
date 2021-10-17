#!/bin/bash

FILE=$1

strings -n 10 $FILE

echo
echo "____ binwalk ____"
binwalk $FILE

echo
echo "____ exiv2 ____"
exiv2 $FILE

echo
echo "____ file ____"
file $FILE

echo
echo "____ todo ____"
echo 'steghide/stegsolve for image files'
echo 'sonic visualiser for audio files'
