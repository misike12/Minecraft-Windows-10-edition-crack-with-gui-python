####################################################
###                                              ###
### THIS FILE WAS MADE BY u/Mino260806 ON REDDIT ###
### PLEASE CREDIT THE AUTHOR IN CASE YOU WANT TO ###
###         PUBLISH IT IN ANY WAY                ###
###                                              ###
####################################################

import subprocess
import time
from pprint import pprint
import re
import sys

while 1:
    tasks = subprocess.check_output('tasklist /apps', shell=True).decode('utf-8', 'ignore').split('\r\n')
    print("#" * 10)
    for i, task in enumerate(tasks):
        if "RuntimeBroker.exe" in task and \
           "MinecraftUWP" in task:
            pid = re.search(r' (\d+) ', task).group(1)
            print(pid)
            output = subprocess.check_output(f'taskkill /f /pid {pid}', shell=True)\
                               .decode('utf-8', 'ignore')
            print(output)
    time.sleep(5)
