#!/usr/bin/python3
import os
import subprocess
from evdev import InputDevice, categorize, ecodes
dev = InputDevice('/dev/input/event13')
dev.grab()

# drop privileges because we do not want to make it to easy for attakcers
os.setuid(1000)
for event in dev.read_loop():
  if event.type == ecodes.EV_KEY:
      key = categorize(event)
      if key.keystate == key.key_down:
          if key.keycode == 'KEY_1':
              # process = subprocess.Popen(["notify-send", "Hallo Welt"])
              os.system("DISPLAY=0 DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus notify-send Hallo Welt")

          elif key.keycode == 'KEY_2':
              os.system("DISPLAY=0 DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus notify-send 'Scan initializing'")
              os.system("scan2paperless")
