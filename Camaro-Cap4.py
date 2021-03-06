# -*- coding: cp936 -*-
"""
Author:zhangbo
Date:2019-09-23
Discription:Read Camaro picture and save 
"""

import cv2,os,time
import numpy as np
from multiprocessing import Process
import thread

class CamaroCap(object):

    #打开摄像头
    def __init__(self):
        #self.cap = cv2.VideoCapture(0)
        self.cap = cv2.VideoCapture("rtsp://admin:admin123@172.16.9.23/cam/realmonitor?channel=1&subtype=0")#获取网络摄像机
        """
        self.cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480);
        """

    #图片信息打印       
    def get_image_info(self,image):
        print(type(image))
        print(image.shape)
        print(image.size)
        print(image.dtype)
        pixel_data = np.array(image)
        print(pixel_data)

    #逐帧读取数据并保存图片到本地制定位置
    def Camaro_image(self):
        i = 0
        #while(1)同while Ture
        while(1):
            """
            ret：True或者False，代表有没有读取到图片
            frame：表示截取到一帧的图片
            """
            ret,frame = self.cap.read()
            ret,frame = self.cap.read()
            #print("打印图片信息")
            #self.get_image_info(frame)
            
            # 展示图片
            cv2.imshow('capture',frame)
            #保存图片
            cv2.imwrite(r"D:\image\\"+ str(i) + ".jpg",frame)
	    #frame.release()
            i = i + 1

            """
            cv2.waitKey(1)：waitKey()函数功能是不断刷新图像，返回值为当前键盘的值
            OxFF：是一个位掩码，一旦使用了掩码，就可以检查它是否是相应的值
            ord('q')：返回q对应的unicode码对应的值(113)
            """
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

if __name__ == '__main__':
    outmasages = CamaroCap()
    #调用摄像头
    outmasages.Camaro_image()
    #释放对象和销毁窗口
    outmasages.cap.release()
    cv2.destroyAllWindows()
    
