import cv2
import random
# read video
webcam = cv2.VideoCapture(0)

faceCase = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
smileCasecade = cv2.CascadeClassifier('haarcascade_smile.xml')



while True:
    # read frame
    ret, frame = webcam.read()
    gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # detect faces
    faces = faceCase.detectMultiScale(gray_scale,  scaleFactor = 1.5, minNeighbors = 5 , minSize = (30, 30))
    #react on faces
    for(x, y, w,h) in faces :
        cv2.rectangle(frame, (x, y), (x + w, y + h), (random.randrange(256), random.randrange(256), random.randrange(256)), 3)
        roi_gray = gray_scale[y:y + h, x:x + w]
        # detect smile
        smile = smileCasecade.detectMultiScale(roi_gray, scaleFactor = 1.5, minNeighbors = 5, minSize = (25, 25))
        for i in smile :
            if len(smile) >1 :
                cv2.putText(frame, 'Thank You For Smiling', (x, y-30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0 ,256,0), 2)

    cv2.imshow('Face Detector', frame)
    cv2.waitKey(1)

       # stop if q is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

webcam.release()

print('Done')

