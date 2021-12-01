#!/bin/bash

COUNT=0
LASTLINE=0

while read line; do
    if [ $line -gt $LASTLINE ]; then
        COUNT=$(($COUNT+1))
    fi
         
    LASTLINE=$line    
done <input.txt

echo $(($COUNT-1))
