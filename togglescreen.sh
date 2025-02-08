#!/bin/bash

#screen1="eDP-1"
#screen2="HDMI-A-1"
screen=${1:-"eDP-1"}

if swaymsg -r -t get_outputs | jq -e --arg screen "$screen" '.[] | select(.name==$screen) | .power' > /dev/null; then
    swaymsg output ${screen} power off
else
    swaymsg output ${screen} power on
fi
