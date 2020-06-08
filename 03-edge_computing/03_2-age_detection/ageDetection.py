# -*- coding: utf-8 -*-
import cv2
import sys
from PIL import Image
import os
from pyagender import PyAgender

def CatchUsbVideo(window_name, camera_idx):
    cv2.namedWindow(window_name)
    agender = PyAgender()
    #視訊來源，可以來自一段已存好的視訊，也可以直接來自USB攝像頭
    cap = cv2.VideoCapture(camera_idx)                
    
    #告訴OpenCV使用人臉識別分類器
    classfier_eye = cv2.CascadeClassifier("haarcascade_eye.xml")
    classfier_face = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
    
    #識別出人臉後要畫的邊框的顏色，RGB格式
    color = (0, 255, 0)
        
    while cap.isOpened():
        ok, frame = cap.read() #讀取一幀資料
        if not ok:            
            break  

        #將當前幀轉換成灰度影象
        grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)                 
        
        #人臉檢測，1.2和2分別為圖片縮放比例和需要檢測的有效點數
        faceRects = classfier_face.detectMultiScale(grey, scaleFactor = 1.2, minNeighbors = 3, minSize = (32, 32))
        
        if len(faceRects) > 0 :            #大於0則檢測到人臉                                   
            for faceRect in faceRects:  #單獨框出每一張人臉
                x, y, w, h = faceRect
                #偵測歲數與性別
                faces = agender.detect_genders_ages(frame[y - 10: y + h + 10, x - 10: x + w + 10])
        #        cv2.rectangle(frame, (x - 10, y - 10), (x + w + 10, y + h + 10), color, 2)                
                if len(faces) >0:          #偵測稻歲數與性別 顯示歲數與性別                    
                    #---------顯示歲數與性別
                    text = "Age : " + str(round(faces[0]['age'],2)) + (" Male" if faces[0]['gender']<0.5 else " Female")
                    org = (x, y-20)
                    fontFace = cv2.FONT_HERSHEY_COMPLEX
                    fontScale = 0.6
                    fontcolor = (255, 0, 0) # BGR
                    thickness = 1 
                    lineType = 4                    
                    cv2.putText(frame, text, org, fontFace, fontScale, fontcolor, thickness, lineType)
                    #--------------------
                '''
                eye_grey=grey[y:y+h, x:x+w]
                eye_color=frame[y:y+h, x:x+w]
                eyeCircle = classfier_eye.detectMultiScale(eye_grey)
                for eyeCle in eyeCircle:
                    ex, ey, ew,eh = eyeCle
                    cv2.circle(eye_color,(int(ex+0.5*ew),int(ey+0.5*eh)),int(ew*0.5),(0,255,0),2)'''
                        
        #顯示影象
        cv2.imshow(window_name, frame)        
        c = cv2.waitKey(5)
        if c & 0xFF == ord('q'):
            break        
    
    #釋放攝像頭並銷燬所有視窗
    cap.release()
    cv2.destroyAllWindows() 
    
if __name__ == '__main__':
    if len(sys.argv) != 1:
        print("Usage:%s camera_id\r\n" % (sys.argv[0]))
    else:
        CatchUsbVideo("Age of face", -1)

