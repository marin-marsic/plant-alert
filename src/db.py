import pickledb

db = pickledb.load('plant_alert.db', False)

def reset(mac):
    db.set('temperature_' + mac, [])
    db.set('moisture_' + mac, [])
    db.set('fertility_' + mac, [])
    db.set('light_' + mac, [])
    db.set('updatedAt_' + mac, 0)

def getList(key, mac):
    dbList = db.get(key + '_' + mac)
    return dbList if (dbList != False) else []

def getTemperatures(mac):
    return getList('temperature', mac)

def insertTemperature(temperature, mac):
    dbList = ([temperature] + getList('temperature', mac))[:4]
    db.set('temperature_' + mac, dbList)
    
def getMoistures(mac):
    return getList('moisture', mac)
    
def insertMoisture(moisture, mac):
    dbList = ([moisture] + getList('moisture', mac))[:4]
    db.set('moisture_' + mac, dbList)
    
def getFertilities(mac):
    return getList('fertility', mac)
    
def insertFertility(fertility, mac):
    dbList = ([fertility] + getList('fertility', mac))[:4]
    db.set('fertility_' + mac, dbList)
    
def getLights(mac):
    return getList('light', mac)
    
def insertLight(light, mac):
    dbList = ([light] + getList('light', mac))[:4]
    db.set('light_' + mac, dbList)
    
def getBattery(mac):
    return db.get('battery_' + mac)
    
def insertBattery(battery, mac):
    db.set('battery_' + mac, battery)
    
def getLastUpdate(mac):
    lastUpdate = db.get('updatedAt_' + mac)
    return lastUpdate if (lastUpdate != False) else 0
    
def insertLastUpdate(updatedAt, mac):
    db.set('updatedAt_' + mac, updatedAt)