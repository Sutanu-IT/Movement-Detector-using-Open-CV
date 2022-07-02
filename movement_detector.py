import winsound
import cv2 as cv

cam=cv.VideoCapture(0) #you can write 1 if 0 is not supporting
while cam.isOpened():  
    ret, frame1 = cam.read() # capturing first frame
    ret, frame2 = cam.read() # capturing second frame
    diff=cv.absdiff(frame2,frame1) # difference between two frames
    gray=cv.cvtColor(diff,cv.COLOR_RGB2GRAY) # making color img to gray img
    blur=cv.GaussianBlur(gray,(5,5),0) # Give a blurry effect
    _ ,thresh=cv.threshold(blur,20,255,cv.THRESH_BINARY) # thresholding the video
    dilated=cv.dilate(thresh,None, iterations=3)  # dialating the img
    contours, _ =cv.findContours(dilated,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE) # making contors over the moving objhects detected by the camera
    #cv.drawContours(frame1,contours,-1,(0,255,0),2) # applying the contours in to the first frame
    for c in contours:  # to eleminate small movements
        if cv.contourArea(c)< 5000:
         continue
        X,Y,W,H=cv.boundingRect(c)
        cv.rectangle(frame1,(X,Y),(X+W,Y+H),(0,255,0),2)
        winsound.Beep(500,200) # you can set another sound if u wish ...  just use   winsound.Playsound('soundfile',winsound.SND_ASYNC)
    
    if cv.waitKey(10)==ord('q'):  # exit statement
        break
    cv.imshow('Mycam', frame1) # final window 
