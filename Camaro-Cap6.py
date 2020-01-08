# -*- coding: cp936 -*-

"""
Author:zhangbo
Date:2019-11-07
Discription:Read Camaro picture and save 
"""

import cv2,os,time,datetime
import numpy as np

class CamaroCap(object):

    """ 打开视频流 """
    def __init__(self):
        
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FPS, 120)
        #VideoWriter，cv2.CAP_DSHOW
        #self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
        #self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)
        self.cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))

    
    """ 图片信息打印 """      
    def get_image_info(self,image):
        print(type(image))
        print(image.shape)
        print(image.size)
        print(image.dtype)
        pixel_data = np.array(image)
        print(pixel_data)


    """ 逐帧读取数据并保存图片到本地制定位置 """
    def Camaro_image(self):
        i = 0
        while(True):
            ret,frame = self.cap.read() #ret：True或者False，代表有没有读取到图片;frame：表示截取到一帧的图片
            if ret == False:
                break
            
            #self.get_image_info(frame) # print("打印图片信息") 注意：调试的时候可以打开，如果是一直运行程序，建议把这行代码注释掉，避免影响内存占用          
            
            cv2.imshow('capture',frame) # 展示图片

            mtime = datetime.datetime.now().strftime('%Y-%m-%d_%H_%M_%S')
            #mtime = datetime.datetime.now().strftime('%M_%S')
            print(mtime)
            
            cv2.imwrite(r"D:\image\\" + str(i) + str("-") + mtime + ".jpg",frame)  # 保存图片
            i = i + 1

            if cv2.waitKey(1) & 0xFF == ord('q'): 
                break
            """
            cv2.waitKey(1)：waitKey()函数功能是不断刷新图像，返回值为当前键盘的值
            OxFF：是一个位掩码，一旦使用了掩码，就可以检查它是否是相应的值
            ord('q')：返回q对应的unicode码对应的值(113)
            """

if __name__ == '__main__':

    outmasages = CamaroCap() # 实例化
    
    outmasages.Camaro_image() # 调用摄像头
    
    outmasages.cap.release() # 释放对象和销毁窗口
    cv2.destroyAllWindows()
    
