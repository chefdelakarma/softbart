#!/bin/bash
# AUTHOR:			BJ Veurink
# NAME: 			setwallpapersway.sh
# LICENSE:		GNU GPLv2

wallpaper=${1}
mode=${mode:-fill}
output=${output:-\*}
expire=${expire:-5000}
if [[ -z $wallpaper ]]; then
	dir=${dir:-/data/wallpapers/distrotube}
	pushd $dir
	mywallpapers=(*.jpg)
	n=${#mywallpapers[@]}
	r=$(( RANDOM % $n ))
	wallpaper=${dir}/${mywallpapers[$r]}
	popd
fi
[[ $(pgrep ^swaybg) ]] && pkill ^swaybg
notify-send -t $expire "wallpaper $wallpaper set"
swaybg -m $mode -o "$output" -i $wallpaper &

