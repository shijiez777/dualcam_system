import cv2

def testDevice(source):
	cap = cv2.VideoCapture(source)
	if cap is None or not cap.isOpened():
		print("camera ", str(source), " not found!")
		return None
	print("found cam ", source)
	return source

cam1No, cam2No = None, None
camNo = 0

while not(cam1No is not None and cam2No is not None):
	if camNo > 10:
		break

	if cam1No is None:
		foundCam = testDevice(camNo)
		if foundCam is not None:
			cam1No = camNo
		camNo += 1
	else:
		foundCam = testDevice(camNo)
		if foundCam is not None:
			cam2No = camNo
		camNo += 1

capLeft = cv2.VideoCapture(cam1No)
capLeft.set(3,160)
capLeft.set(4,120)

capRight = cv2.VideoCapture(cam2No)
capRight.set(3,160)
capRight.set(4,120)

# create old frame
_, frameLeft = capLeft.read()
_, frameRight = capRight.read()

cv2.namedWindow('Left cam')
cv2.namedWindow('Right cam')

while True:
    _, frameLeft = capLeft.read()
    _, frameRight = capRight.read()

    cv2.imshow('Left cam', frameLeft)
    cv2.imshow('Right cam', frameRight)

    if cv2.waitKey(1) & 0xFF == ord('q'):
    	break

capLeft.release()
capRight.release()
cv2.destroyAllWindows()
