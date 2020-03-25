#!/usr/bin/python3.7
import subprocess
import re
import time
import syslog

while (1):
    time.sleep(3600)
    res = subprocess.run(["ping", "-c", "4", "-W", "2", "10.0.1.1"], capture_output=True)

    if not re.search("100% packet loss", str(res.stdout)):
        # success
        pass
    else:
        # no network or server down. restart
        syslog.syslog(syslog.LOG_CRIT, "[Network watchdog] Could not reach 10.0.1.1, rebooting!\n")
        print('Could not reach 10.0.1.1, rebooting!\n')
        subprocess.run(["reboot"])


