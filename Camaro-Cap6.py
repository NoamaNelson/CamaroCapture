# -*- coding: cp936 -*-

"""
Author:zhangbo
Date:2019-11-07
Discription:Read Camaro picture and save 
"""

import cv2,os,time,datetime
import numpy as np

class CamaroCap(object):

    """ ����Ƶ�� """
    def __init__(self):
        
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FPS, 120)
        #VideoWriter��cv2.CAP_DSHOW
        #self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
        #self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)
        self.cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))

    
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
            
            #self.get_image_info(frame) # print("��ӡͼƬ��Ϣ") ע�⣺���Ե�ʱ����Դ򿪣������һֱ���г��򣬽�������д���ע�͵�������Ӱ���ڴ�ռ��          
            
            cv2.imshow('capture',frame) # չʾͼƬ

            mtime = datetime.datetime.now().strftime('%Y-%m-%d_%H_%M_%S')
            #mtime = datetime.datetime.now().strftime('%M_%S')
            print(mtime)
            
            cv2.imwrite(r"D:\image\\" + str(i) + str("-") + mtime + ".jpg",frame)  # ����ͼƬ
            i = i + 1

            if cv2.waitKey(1) & 0xFF == ord('q'): 
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
    
