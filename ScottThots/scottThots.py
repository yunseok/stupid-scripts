#!/usr/bin/env python

import subprocess
import win32gui
import time

# TO ADD MORE EPISODES WHERE JAN IS SINGING
scottTotts = 'The Office S06E12 - VLC media player'
dinnerParty = 'The Office S04E13 - VLC media player'

while True:
    if scottTotts == win32gui.GetWindowText(win32gui.GetForegroundWindow()):
        skipIt = "vlc --key-next alt-n"
        process = subprocess.Popen(skipIt.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        continue
    if dinnerParty = win32gui.GetWindowText(win32gui.GetForegroundWindow()):
        skipIt = "vlc --key-next alt-n"
        process = subprocess.Popen(skipIt.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        continue
    else
        continue
    time.sleep(900)
