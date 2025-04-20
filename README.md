# Shelly1-into-DBUS-Victron
A simple script to use the GUI relay switch to send on off signals via http to a Shelly 1 wifi relais

#requirements:
A (wifi) network where the Venus OS device (raspberry pi works, I don't know if it works with a Cerbo) and a Shelly 1 wifi relais are connected to
Static IP for the SHelly relais
SSH connection to the raspberry pi (internet(tailscale works awesome) or local)

What this script essentially does is mirroring the GUI signals from the desired Relay (1 in my case) to send on off signals via http to the shelly relay.
So when toggeling the relay in the gui it sends a signal on the DBUS. This signal is picked up and used to trigger commands via http.
note: relay 1 in the gui is relay 0 on the DBUS

The other script is to start it on boot


