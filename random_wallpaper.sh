#!/bin/bash

mode=${mode:-fill}
output=${output:-\*}

# Directory containing wallpapers
WALLPAPER_DIR="/usr/share/wallpapers/distrotube"

# Select a random wallpaper
RANDOM_WALLPAPER=$(find "$WALLPAPER_DIR" -type f | shuf -n 1)

[[ $(pgrep ^swaybg) ]] && pkill ^swaybg

# Set the wallpaper
swaybg -m $mode -o "$output" -i $RANDOM_WALLPAPER &
