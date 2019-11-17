import subprocess
import time
import os


def process_exists(process_name):
    call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
    output = subprocess.check_output(call)
    last_line = output.strip().split('\r\n')[-1]
    return last_line.lower().startswith(process_name.lower())

while True:
    if (process_exists('Notifier.exe')):
        os.system('taskkill /f /im Notifier.exe')
        continue
    else:
        time.sleep(5)
