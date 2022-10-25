import cv2

capture = cv2.VideoCapture(0)

while True:
    _, frame = capture.read()
    cv2.imshow("pic", frame)

    if cv2.waitKey(10) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
