import datetime
import time
import socket
import math
#coding:utf-8


def getData():
    s = socket.socket()    
    s.connect(('192.168.43.168',8181))
    # s.send("connect")
    # coord = s.recv(1024).decode()
    coord = s.recv(1024).decode()
    # s.close()
    type,place=coord.split(':')
    if type.find('location')!=-1:
        lati,longi=place.split(',')
        #lati,longi=place.split(',')
        # lati, longi,bearing,speed,accuracy,time = place.split(',')
        lati = round(float(lati),5)
        longi = round(float(longi),5)

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
    UTCsecond =int(time.mktime(time.localtime()))*1000
    ST = UTCsecond
    #print("----"+str(time.mktime(time.localtime())))
    return ST,lati,longi

if __name__ == '__main__':
    while(True):
        y = getData()
        print(y)
    