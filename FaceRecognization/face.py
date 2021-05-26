import cv2
face_cascade=cv2.CascadeClassifier("haarcascade_frontalcatface.xml")
def detect():
    capture=cv2.VideoCapture(0)
    while True:
        _,image=capture.read()
        gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        face=face_cascade.detectMultiScale(gray,1.1,4)
        for (x,y,w,h) in face:
            cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.imshow("Face Detected",image)
        if cv2.waitKey(1)==27:
            break
    capture.release()
detect()
