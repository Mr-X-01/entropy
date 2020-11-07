# Author: Mr-X-01
# Telegram: @Mrxanon
# https://github.com/Mr-X-01

import subprocess
import time
START=time.time()
while True:
    time.sleep(60)
    end_time=time.time()
    if end_time - START > 300:
        break
    subprocess.Popen("echo 'b' >> /tmp/replace",shell=True)
