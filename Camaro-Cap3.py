# -*- coding: cp936 -*-
"""
Author:zhangbo
Date:2019-09-23
Discription:Read Camaro picture and save 
"""

import cv2,os,time
import numpy as np
from multiprocessing import Process

class CamaroCap(object):

    #������ͷ
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        
    #ͼƬ��Ϣ��ӡ       
    def get_image_info(self,image):
        print(type(image))
        print(image.shape)
        print(image.size)
        print(image.dtype)
        pixel_data = np.array(image)
        print(pixel_data)

    #��֡��ȡ���ݲ�����ͼƬ�������ƶ�λ��
    def Camaro_image(self):
        i = 0
        #while(1)ͬwhile Ture
        while(1):
            """
            ret��True����False��������û�ж�ȡ��ͼƬ
            frame����ʾ��ȡ��һ֡��ͼƬ
            """
            ret,frame = self.cap.read()
            print("��ӡͼƬ��Ϣ")
            self.get_image_info(frame)
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

if __name__ == '__main__':
    outmasages = CamaroCap()
    #��������ͷ
    m = Process(target=outmasages.Camaro_image(), args=(5, ))
    m.start()
    for i in range(5):
        print("������ִ����--%d--pid=%s" % (i, os.getpid()))
        time.sleep(0.5)
    #outmasages.Camaro_image()
    #�ͷŶ�������ٴ���
    outmasages.cap.release()
    cv2.destroyAllWindows()
    
