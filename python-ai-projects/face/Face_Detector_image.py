# face detecor application
import cv2
import random
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
 
img = cv2.imread('face.jpg')

#convert grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Detect faces
faces = trained_face_data.detectMultiScale(gray_img)

#draw circle around the faces
for(x,y,w,h) in faces:
    cv2.rectangle(img, (x, y), (x + w , y+h),(random.randrange(256) ,random.randrange(256),random.randrange(256)), 10)


cv2.imshow('Face Detector', img)
cv2.waitKey()


print("code completed")