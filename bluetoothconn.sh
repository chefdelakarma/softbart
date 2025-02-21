#!/bin/bash

# Vervang dit met het MAC-adres van je Bluetooth-apparaat
DEVICE_MAC="xx:xx:xx:xx:xx:xx"

# Zet Bluetooth aan
rfkill unblock bluetooth

# Start bluetoothctl en voer commando's uit
if bluetoothctl << EOF
power on
agent on
default-agent
connect $DEVICE_MAC
EOF
then
	notify-send "Verbonden met $DEVICE_MAC"
else
	notify-send "bluetooth connect error"
fi
