
# sensor mac addresses
macAddresses = ["c4:7c:8d:66:4d:0d"]

# min and max moisture (%)
moisture = [15, 60]

# min and max temperature (°C)
temperature = [8, 35]

# min and max fertility (uS/cm)
fertility = [350, 2000]

# min and max light (lux)
light = [4000, 76000]

# battery level alert (%)
battery = 5

# IFTTT webhook url
webhookUrl = 'https://maker.ifttt.com/trigger/plant-alert/with/key/iV0vrIav7ejZyhJzcANcDTrM_gfQbGYQJrgNPhjoafW'

# cron scheduling https://pypi.org/project/python-crontab/
# the coldest, the warmest time of day, morning, noon and evening sunlight
cronTiming = '1 4,9,13,18 * * *'
