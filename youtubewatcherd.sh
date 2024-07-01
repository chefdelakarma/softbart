#!/bin/bash
# use with wl-paste --watch thisscript
options=${options:-"--no-playlist"}
format=${format:-"ba"}
output=${output:-"%(title)s.%(ext)s"}
expire_notify=${expire_notify:-5000}
clipboard=$(wl-paste 2>/dev/null)
if [[ $clipboard =~ ^(https?\:\/\/)?((www\.|music\.)?youtube\.com|youtu\.be)\/.+$ ]]; then
	title=$(yt-dlp --get-title $clipboard )
	notify-send -t ${expire_notify} "yt-dlp: ${title}"
	yt-dlp --format $format $options -o $output $clipboard
else
	echo "is not a rigth URL to youtube"
	echo "link= $clipboard"
fi
