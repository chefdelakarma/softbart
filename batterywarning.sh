#!/bin/bash

expire=${expire:-10000}
notify-send -t ${expire} "Battery Warning Alert ON"
critical_bat_capacity=${critical_bat_capacity:-20}

while true; do
		bat_status=$(cat /sys/class/power_supply/BAT0/status)
		bat_capacity=$(cat /sys/class/power_supply/BAT0/capacity)

		[[ ${bat_status} == "Discharging" && ${bat_capacity} -le ${critical_bat_capacity} ]] && notify-send -t ${expire} --urgency=critical "BATTERY WARNING: Low and Discharging" "BATTERY CAPACITY=${bat_capacity}"
		sleep 300
done
