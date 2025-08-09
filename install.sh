#!/bin/sh
set -e

REPO_BASE="https://raw.githubusercontent.com/OWNER/Shelly1-into-DBUS-Victron/main"
TARGET_DIR=/data

# Download scripts
curl -fsSL "$REPO_BASE/shelly-follow-relay0.py" -o "$TARGET_DIR/shelly-follow-relay0.py"
chmod +x "$TARGET_DIR/shelly-follow-relay0.py"

curl -fsSL "$REPO_BASE/rc.local" -o "$TARGET_DIR/rc.local"
chmod +x "$TARGET_DIR/rc.local"

echo "Installation complete. Reboot to start the service."
