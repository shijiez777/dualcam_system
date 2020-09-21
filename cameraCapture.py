import cv2

cap = cv2.VideoCapture(2)

_, frame = cap.read()

while True:
    _, frame = cap.read()

    cv2.imwrite( "2.jpg", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
