@echo off
ffmpeg -i %1 -vn -ar 44100 -ac 2 -ab 192k -f mp3 %1.mp3
@echo on