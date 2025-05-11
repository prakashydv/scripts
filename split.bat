ffmpeg -i "%1" -f segment -segment_time 300 -c copy "%1_%%03d.mp3"
