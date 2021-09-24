import datetime
import time
import socket
import math
#coding:utf-8


def getData(client):
    # s.send("connect")
    # coord = s.recv(1024).decode()
    coord = client.recv(1024).decode()
    # s.close()
    place = ''
    print(coord)
    try:
        type, place = coord.split(':')
    except:
        print('error')
    if (len(place) <= 0):
        return None
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
    if(longi>0):
        a = 1
    else:
        a = -1
    '''
    timezone = math.floor((longi+7.5*(a))/15)
    UTCh = datetime.datetime.utcnow().hour
    ST = timezone + UTCh
    UTCm = datetime.datetime.utcnow().minute
    ST=ST+float(UTCm)/100
    '''
    # 获取时间戳
    current = str(time.time() * 1000)
    UTCsecond,two = current.split('.')
    ST = int(UTCsecond)
    #print("----"+str(time.mktime(time.localtime())))
    return ST,lati,longi,bearing,speed,accuracy,locationTime

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, True)
    s.ioctl(socket.SIO_KEEPALIVE_VALS, (1, 60 * 1000, 30 * 1000))
    s.connect(('192.168.43.168', 8181))
    while(True):
        y = getData(s)
        # print(y)
    