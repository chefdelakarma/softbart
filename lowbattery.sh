#!/bin/bash

bat_capacity=$(cat /sys/class/power_supply/BAT0/capacity)
expire=${expire:-60000}

notify-send -t ${expire} --urgency=critical "BATTERY WARNING: Low and discharging" "BATTERY CAPACITY=${bat_capacity}%"
