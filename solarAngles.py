# 阳光角度
import math
import time
import datetime


def solarAngles(longitude,latitude):
    longi = longitude
    lati = latitude
    localtime = time.localtime(time.time())
    dec = 23.45*math.sin(math.radians(360*(284+localtime.tm_yday)/365))
    if(longi>0):
        a = 1
    else:
        a = -1
    timezone = int((longi+7.5*(a))/15)
    UTCh = datetime.datetime.utcnow().hour
    ST = timezone + UTCh
    h=15*(ST-12)
    solaraltitudesin = math.cos(math.radians(h))*math.cos(math.radians(dec))*math.cos(math.radians(lati))+math.sin(math.radians(dec))*math.sin(math.radians(lati))
    solaraltitude = math.degrees(math.asin(solaraltitudesin))
    solarazimuthcos = (math.sin(math.radians(dec))-math.sin(math.radians(solaraltitude))*math.sin(math.radians(lati)))/(math.cos(math.radians(solaraltitude))*math.cos(math.radians(lati)))
    solarazimuth = math.degrees(math.acos(solarazimuthcos))
    # print(h)
    if(h>=0):
        solarazimuth = - solarazimuth
    return round(solaraltitude,2),round(solarazimuth,2)


if __name__ == '__main__':
    longitude = 121.47
    latitude = 31.23
    y = solarAngles(longitude,latitude)
    print(y)