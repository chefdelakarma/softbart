#!/bin/bash


# Vervang dit met het MAC-adres van je Bluetooth-apparaat
DEVICE_MAC=""

if bluetoothctl info $DEVICE_MAC | grep -q "Connected: yes"; then
	bluetoothctl disconnect $DEVICE_MAC
	notify-send "Disconnect $DEVICE_MAC"
	exit 0
fi

# Zet Bluetooth aan
rfkill unblock bluetooth
sleep 5

# Start bluetoothctl en voer commando's uit
bluetoothctl << EOF
power on
agent on
default-agent
trust $DEVICE_MAC
pair $DEVICE_MAC
EOF
sleep 5
bluetoothctl connect $DEVICE_MAC


if bluetoothctl info $DEVICE_MAC | grep -q "Connected: yes"; then
	notify-send "Connected $DEVICE_MAC" 
else
	notify-send "error bluetooth"
fi
