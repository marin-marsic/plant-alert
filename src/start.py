import os
from crontab import CronTab
from config import cronTiming
from config import *
from db import *

for mac in macAddresses:
    reset(mac)
    
db.dump()

cron = CronTab(user = True)
dirName = os.path.dirname(__file__)
dirName = os.path.realpath(dirName)
scriptPath = dirName + '/refresh.py'
job = cron.new(command='python3 ' + scriptPath, comment='plant-alert')
job.setall(cronTiming)

for job in cron:
    print(job)

cron.write()