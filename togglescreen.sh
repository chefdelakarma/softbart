#!/bin/bash
#!/bin/bash
# AUTHOR:			BJ Veurink
# NAME: 			toggle swayscreen
# LICENSE:		GNU GPLv2

#screen1="eDP-1"
#screen2="HDMI-A-1"
screen=${1:-"eDP-1"}
expire=${expire:-5000}
if swaymsg -r -t get_outputs | jq -e --arg screen "$screen" '.[] | select(.name==$screen) | .power' > /dev/null; then
    swaymsg output ${screen} power off
    notify-send -t $expire "screen ${screen} off"
else
    swaymsg output ${screen} power on
fi

pkill -f ^swayidle
mapfile -t screens_on < <(swaymsg -r -t get_outputs | jq -r '.[] | select(.power == true) | .name')

swayidle -w \
    timeout 300 "$(for screen in "${screens_on[@]}"; do echo "swaymsg output $screen power off"; done)" \
    resume "$(for screen in "${screens_on[@]}"; do echo "swaymsg output $screen power on"; done)" &

notify-send -t $expire "swayidle on" "${screens_on[@]}"
