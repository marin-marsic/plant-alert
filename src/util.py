from db import *


emojiAlert = '\U000026A0'
emojiOk = '\U0001F49A'

def getEmoticon(positive):
    if positive:
        return emojiOk
    return emojiAlert

def checkValue(dbValues, valRange, requireAll):
    valOk = True if requireAll else False
    for dbVal in dbValues:
        if (requireAll):
            if (dbVal < valRange[0] or dbVal > valRange[1]):
                valOk = False
        elif (dbVal >= valRange[0] and dbVal <= valRange[1]):
            valOk = True
          
    return valOk
