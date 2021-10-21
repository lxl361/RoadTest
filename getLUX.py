# 主程序
# !/usr/bin/python
#coding:utf-8
import serial
from getdata import getData
from solarAngles import solarAngles


if __name__ == '__main__':
        serial = serial.Serial('COM1841','9600')
        if serial.isOpen():
                print('串口打开成功！\n')
                f = open('./data/LUX09291.txt','a') #若需保留原数据则改为f = open('./try.txt','a')
                #pass
        else :
                print('串口打开失败！\n')
        try:
                wholedata = ''
                while True:
                        count = serial.inWaiting()
                        if count > 0:
                                # data = serial.read(count)
                                # print(type(data))
                                # read数据的时候需要解码，然后数据有误会出现特殊字符
                                data = serial.read(count).decode()
                                i = 0
                                while i<len(data):
                                        if data[i] == '#':
                                                elsedata = getData()
                                                if (len(elsedata) == 0):
                                                   continue
                                                for item in elsedata:
                                                        if (len(item) == 0):
                                                                continue
                                                        solarAngleData = solarAngles(item[2], item[1])
                                                        alldata = str(wholedata) + ' ' + str(item[0]) + ' ' + str(
                                                                item[1]) + ' ' + str(item[2]) + ' ' + str(
                                                                solarAngleData[0]) + ' ' + str(
                                                                solarAngleData[1]) + ' ' + str(item[3]) + ' ' + str(
                                                                item[4]) + ' ' + str(item[5]) + ' ' + str(
                                                                item[6])
                                                        # alldata = alldata + ' ' + str(elsedata[4])+ ' ' + str(elsedata[5])+ ' ' + str(elsedata[6])
                                                        # 光强，时间，纬度，经度，太阳仰角，太阳偏离北方的角度（根据东西分正负,东边正值西边负值）
                                                        # print('data:'+alldata)
                                                        print(alldata)
                                                        # f.write(alldata.decode('utf-8'))
                                                        f.write(alldata)
                                                        f.write('\n')
                                                        # flush实现实时数据的写入，避免文件未正常关闭下，无法正常写入数据
                                                        f.flush()
                                                        # f.write('\n')
                                                wholedata = ''
                                                i = i + 1
                                        else:
                                                wholedata += data[i]
                                                i = i+1


        except KeyboardInterrupt:
                if serial != None:
                        f.close()
                        serial.close()