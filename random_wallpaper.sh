#!/bin/bash
export WAYLAND_DISPLAY=wayland-1
export SWAYSOCK=$(ls /run/user/$(id -u)/sway-ipc.*.sock)
export I3SOCK=$(ls /run/user/$(id -u)/sway-ipc.*.sock)
export XDG_SEAT=seat0
export XDG_VTNR=1
export XDG_SESSION_ID=1
export XDG_RUNTIME_DIR=/run/user/1000

# Directory containing wallpapers
WALLPAPER_DIR="/usr/share/wallpapers"

# Select a random wallpaper

mapfile -t allscreens < <(swaymsg -r -t get_outputs | jq -r '.[] | .name')

[[ $(pgrep ^swaybg) ]] && pkill ^swaybg
for screen in "${allscreens[@]}"; do
	RANDOM_WALLPAPER=$(find "$WALLPAPER_DIR" -type f -name "*.jpg" | shuf -n 1)
	swaybg -m fill -o "${screen}" -i "${RANDOM_WALLPAPER}" &
done
