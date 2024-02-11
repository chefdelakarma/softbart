#!/bin/bash
# AUTHOR:			BJ Veurink
# NAME: 			toggle swayidle
# LICENSE:		GNU GPLv2

expire=${expire:-5000}
if [[ $(pgrep ^swayidle) ]]; then
	notify-send -t $expire "swayidle off"
	pkill ^swayidle
else
	notify-send -t $expire "swayidle on"
	#swayidle -w timeout 300 'swaylock -f -c 0000ff' timeout  120 'swaymsg "output * dpms off"' resume 'swaymsg "output * dpms on"'  before-sleep 'swaylock -f -c ff0000'
	swayidle -w timeout 120 'swaymsg "output * dpms off"' resume 'swaymsg "output * dpms on"'
fi
