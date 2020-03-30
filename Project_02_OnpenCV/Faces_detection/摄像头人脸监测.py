import numpy as np
import cv2

# 从摄像头获取图像数据
cap = cv2.VideoCapture(0)

while(True):
    # ret 读取成功True或失败Falseq
    # frame读取到的图像的内容
    # 读取一帧数据
    ret,frame = cap.read()
    frame = cv2.flip(frame,1)#水平翻转
    detector = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
    rects = detector.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=2, minSize=(10,10), flags=cv2.CASCADE_SCALE_IMAGE)
    for (x,y,w,h) in rects:
    # 画矩形框
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
    cv2.imshow('frame',frame)
    # waitKey功能是不断刷新图像，单位ms，返回值是当前键盘按键值
    # ord返回对应的ASCII数值
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
