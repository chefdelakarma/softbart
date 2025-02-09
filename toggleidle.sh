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
swayidle -w \
    timeout 300 "$(for screen in "${screens_on[@]}"; do echo "swaymsg output $screen power off"; done)" \
    resume "$(for screen in "${screens_on[@]}"; do echo "swaymsg output $screen power on"; done)" &
fi
