#!/bin/bash
if [ -z "$1" ]; then
    echo "No filename provided"
    exit 1
fi

inputname="$1"
outputname="$2"
fonttools.exe feaLib -o "$outputname" features.fea "$inputname" && ttx -o "$outputname.ttx" "$outputname"