# -*- coding: cp936 -*-
"""
Author:zhangbo
Date:2019-09-23
Discription:Read Camaro cature and save
"""

import cv2
import numpy as np


#������ͷ
cap = cv2.VideoCapture(0)
    
#ͼƬ��Ϣ��ӡ       
def get_image_info(image):
    print(type(image))
    print(image.shape)
    print(image.size)
    print(image.dtype)
    pixel_data = np.array(image)
    print(pixel_data)

#��֡��ȡ���ݲ�����ͼƬ�������ƶ�λ��
def Camaro_image():
    i = 0
    #while(1)ͬwhile Ture
    while(1):
        """
        ret��True����False��������û�ж�ȡ��ͼƬ
        frame����ʾ��ȡ��һ֡��ͼƬ
        """
        ret,frame = cap.read()
        print(frame)
        print("��ӡͼƬ��Ϣ")
        get_image_info(frame)
        # չʾͼƬ
        cv2.imshow('capture',frame)
        #����ͼƬ
        cv2.imwrite(r"D:\image\\"+ str(i) + ".jpg",frame)
        i = i + 1
        """
        cv2.waitKey(1)��waitKey()���������ǲ���ˢ��ͼ�񣬷���ֵΪ��ǰ���̵�ֵ
        OxFF����һ��λ���룬һ��ʹ�������룬�Ϳ��Լ�����Ƿ�����Ӧ��ֵ
        ord('q')������q��Ӧ��unicode���Ӧ��ֵ(113)
        """
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

Camaro_image()
#�ͷŶ�������ٴ���
cap.release()
cv2.destroyAllWindows()

