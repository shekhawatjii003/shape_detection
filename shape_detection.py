import cv2
import numpy as np
def empty(a):
    pass
cv2.namedWindow('PARAMETERS')
cv2.resizeWindow('PARAMETERS',640,240)
cv2.createTrackbar('threshold1', 'PARAMETERS', 23, 255, empty)
cv2.createTrackbar('threshold2','PARAMETERS',22,255,empty)

def getcontours(img,imgcontour):
    contours,hirearchy=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 1000:
            cv2.drawContours(imgcontour,cnt,-1,(0,255,0),7)
            peri=cv2.arcLength(cnt,True)
            approx=cv2.approxPolyDP(cnt,0.02*peri,True)




def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

cap=cv2.VideoCapture(1)
while(True):
    success,img=cap.read()
    imgcontour=img.copy()

    imgblur=cv2.GaussianBlur(img,(7,7),1)
    imgblur2gray=cv2.cvtColor(imgblur,cv2.COLOR_BGR2GRAY)
    threshold1=cv2.getTrackbarPos('threshold1','PARAMETERS')
    threshold2=cv2.getTrackbarPos('threshold2','PARAMETERS')
    imgcanny=cv2.Canny(imgblur,threshold1,threshold2)
    kernel=np.ones((5,5),np.uint8)
    dil=cv2.dilate(imgcanny,kernel,iterations=1)
    contour=getcontours(dil,imgcontour)
    stack=stackImages(0.7,([img,imgblur2gray,imgcanny],[dil, imgcontour, imgcontour]))

    cv2.imshow('STACK IMAGEE', stack)


    if cv2.waitKey(1) & 0xFF == ord('q'):\

        break
cap.release()
cv2.destroyAllWindows()