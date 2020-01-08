# -*- coding: cp936 -*-

"""
Author:zhangbo
Date:2019-11-07
Discription:Read Camaro picture and save 
"""

import cv2,os,time
import numpy as np

class CamaroCap(object):

    """ ����Ƶ�� """
    def __init__(self):

        self.cap = cv2.VideoCapture("./MVI_1637.MOV")  # ��Ƶ·����ֱ�Ӱѽű�����Ƶ����ͬһ��Ŀ¼����ã�Ҳ����ָ����Ӧ����Ƶ·��

    """ ͼƬ��Ϣ��ӡ """      
    def get_image_info(self,image):
        print(type(image))
        print(image.shape)
        print(image.size)
        print(image.dtype)
        pixel_data = np.array(image)
        print(pixel_data)

    """ ��֡��ȡ���ݲ�����ͼƬ�������ƶ�λ�� """
    def Camaro_image(self):
        i = 0
        while(True):
            ret,frame = self.cap.read() #ret��True����False��������û�ж�ȡ��ͼƬ;frame����ʾ��ȡ��һ֡��ͼƬ
            if ret == False:
                break
            
            self.get_image_info(frame) # print("��ӡͼƬ��Ϣ") ע�⣺���Ե�ʱ����Դ򿪣������һֱ���г��򣬽�������д���ע�͵�������Ӱ���ڴ�ռ��          
            
            cv2.imshow('capture',frame) # չʾͼƬ
            
            cv2.imwrite(r"D:\image\\"+ str(i) + ".jpg",frame)  # ����ͼƬ
            i = i + 1

            if cv2.waitKey(1) & 0xFF == ord('q'): # 
                break
            """
            cv2.waitKey(1)��waitKey()���������ǲ���ˢ��ͼ�񣬷���ֵΪ��ǰ���̵�ֵ
            OxFF����һ��λ���룬һ��ʹ�������룬�Ϳ��Լ�����Ƿ�����Ӧ��ֵ
            ord('q')������q��Ӧ��unicode���Ӧ��ֵ(113)
            """

if __name__ == '__main__':

    outmasages = CamaroCap() # ʵ����
    
    outmasages.Camaro_image() # ��������ͷ
    
    outmasages.cap.release() # �ͷŶ�������ٴ���
    cv2.destroyAllWindows()
    
