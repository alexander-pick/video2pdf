#!/bin/bash

find . -name '*.mp4' -exec extract.py {} \;
find * -prune -type d | while IFS= read -r d; do 
 cd "$d"
	ti=$(date +%s)
	convert *.png ../$ti.pdf
 cd ..
done