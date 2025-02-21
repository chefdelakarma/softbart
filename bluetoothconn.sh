#!/bin/bash

# Vervang dit met het MAC-adres van je Bluetooth-apparaat
DEVICE_MAC="xx:xx:xx:xx:xx:xx"

# Zet Bluetooth aan
rfkill unblock bluetooth
sleep 2

# Start bluetoothctl en voer commando's uit
if bluetoothctl << EOF
power on
agent on
default-agent
trust $DEVICE_MAC
pair $DEVICE_MAC
connect $DEVICE_MAC
EOF
then
	notify-send "Verbonden met $DEVICE_MAC"
else
	notify-send "bluetooth connect error"
fi

# Controleer of de verbinding succesvol is, zo niet, probeer opnieuw
for i in {1..3}; do
    if bluetoothctl info $DEVICE_MAC | grep -q "Connected: yes"; then
        echo "Succesvol verbonden met $DEVICE_MAC"
        exit 0
    fi
    echo "Verbinding mislukt, opnieuw proberen ($i/3) ..."
    sleep 2
    bluetoothctl connect $DEVICE_MAC
done

echo "Kon geen verbinding maken met $DEVICE_MAC."
