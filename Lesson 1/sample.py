#    __author__ = 'YANER'
#    __date__ = '2018/7/24'
#    __Desc__ = 测试opencv的Python环境是否搭建成功
import sys
import cv2
image = cv2.imread('C:\\Users\\jiance04\\Desktop\\1.tif')
cv2.namedWindow("MyImage",0)
cv2.imshow("MyImage",image)
cv2.waitKey(0)