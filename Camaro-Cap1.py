# -*- coding: cp936 -*-
"""
Author:zhangbo
Date:2019-09-23
Discription:Read Camaro cature and save
"""

import cv2
import numpy as np


#打开摄像头
cap = cv2.VideoCapture(0)
    
#图片信息打印       
def get_image_info(image):
    print(type(image))
    print(image.shape)
    print(image.size)
    print(image.dtype)
    pixel_data = np.array(image)
    print(pixel_data)

#逐帧读取数据并保存图片到本地制定位置
def Camaro_image():
    i = 0
    #while(1)同while Ture
    while(1):
        """
        ret：True或者False，代表有没有读取到图片
        frame：表示截取到一帧的图片
        """
        ret,frame = cap.read()
        print(frame)
        print("打印图片信息")
        get_image_info(frame)
        # 展示图片
        cv2.imshow('capture',frame)
        #保存图片
        cv2.imwrite(r"D:\image\\"+ str(i) + ".jpg",frame)
        i = i + 1
        """
        cv2.waitKey(1)：waitKey()函数功能是不断刷新图像，返回值为当前键盘的值
        OxFF：是一个位掩码，一旦使用了掩码，就可以检查它是否是相应的值
        ord('q')：返回q对应的unicode码对应的值(113)
        """
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

Camaro_image()
#释放对象和销毁窗口
cap.release()
cv2.destroyAllWindows()

