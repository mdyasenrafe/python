import cv2
import random
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# video capture
webcam = cv2.VideoCapture(0)

while True : 
    webcam_read, frame = webcam.read()
    #convert to grayscale
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #Detect faces

    faces = trained_face_data.detectMultiScale(gray_img)
    #draw circle around the faces
    for(x,y,w,h) in faces:
        cv2.rectangle(frame, (x, y), (x + w , y+h),(random.randrange(256) ,random.randrange(256),random.randrange(256)), 5)
    cv2.imshow('Face Detector', frame)
    cv2.waitKey(1)
    # stop if q is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

webcam.release()

