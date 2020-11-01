from crontab import CronTab

cron = CronTab(user = True)
cron.remove_all(comment='plant-alert')

cron.write()