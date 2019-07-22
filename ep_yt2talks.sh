#!/bin/bash

youtube-dl -q -f 140 "$1" -o - | \
    ffmpeg -loglevel quiet -i -   -acodec pcm_s16le -ac 1 -f wav  - | \
    auditok -i - -r 44100 -w 2 -c 1 > /tmp/$$.detect.txt

python3 join_detection.py /tmp/$$.detect.txt
rm /tmp/$$.detect.txt
