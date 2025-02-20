#!/bin/bash

# Vervang dit met het MAC-adres van je Bluetooth-apparaat
DEVICE_MAC="${1}"

# Zet Bluetooth aan
rfkill unblock bluetooth

# Start bluetoothctl en voer commando's uit
bluetoothctl << EOF
power on
agent on
default-agent
connect $DEVICE_MAC
EOF

echo "Verbonden met $DEVICE_MAC"

