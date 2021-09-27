import datetime
import time
import socket
import math
#coding:utf-8

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, True)
s.ioctl(socket.SIO_KEEPALIVE_VALS, (1, 60 * 1000, 30 * 1000))
s.connect(('192.168.43.168', 8181))

def getData():
    # s.send("connect")
    # coord = s.recv(1024).decode()
    coord = s.recv(1024).decode()
    # s.close()
    place = ''
    result = []
    try:
        list = coord.split('\n')
        for item in list:
            if len(item) != 0:
                type, place = item.split(':')
                temp = convertLatLongs(type, place)
                result.append(temp)
    except:
        print('error')
    '''
    timezone = math.floor((longi+7.5*(a))/15)
    UTCh = datetime.datetime.utcnow().hour
    ST = timezone + UTCh
    UTCm = datetime.datetime.utcnow().minute
    ST=ST+float(UTCm)/100
    '''

    # 获取时间戳
    print(result)
    #print("----"+str(time.mktime(time.localtime())))
    return result

def convertLatLongs(type, place):
    if (len(place) <= 0):
        return []
    if type.find('location')!=-1:
        # lati,longi,=place.split(',')
        #lati,longi=place.split(',')
        lati, longi,bearing,speed,accuracy,locationTime = place.split(',')
        lati =float(lati)
        longi =float(longi)
        bearing=float(bearing)
        speed=float(speed)
        accuracy=float(accuracy)
        locationTime=int(locationTime)
        current = str(time.time() * 1000)
        UTCsecond, two = current.split('.')
        ST = int(UTCsecond)
        return [ST, lati, longi,bearing,speed,accuracy,locationTime]
    return []

if __name__ == '__main__':
    while(True):
        y = getData()
        # print(y)
    