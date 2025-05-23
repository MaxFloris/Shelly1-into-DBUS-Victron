#!/usr/bin/env python3
import dbus
import dbus.mainloop.glib
from gi.repository import GLib
import requests
import time

# Replace with your actual Shelly IP
SHELLY_IP = "REPLACE WITH YOUR SHELLY IP"

def toggle_shelly(state):
    try:
        # Debounce delay to avoid rapid changes on boot
        time.sleep(0.1)
        url = f"http://{SHELLY_IP}/relay/0?turn={'on' if state else 'off'}"
        requests.get(url, timeout=3)
    except Exception:
        pass  # Fail silently (network or device might not be up yet)

# D-Bus signal handler (only 1 argument on your system)
def on_change(changed):
    if "Value" in changed:
        value = int(changed["Value"])
        toggle_shelly(value)

def main():
    # Force Shelly OFF at startup
    toggle_shelly(0)

    # Setup D-Bus listener
    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
    bus = dbus.SystemBus()
    bus.add_signal_receiver(
        handler_function=on_change,
        signal_name="PropertiesChanged",
        dbus_interface="com.victronenergy.BusItem",
        path="/Relay/0/State"
    )

    GLib.MainLoop().run()

if __name__ == "__main__":
    main()
