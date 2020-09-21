import cv2
import numpy as np

def nothing(x):
    pass

frameWidth = 1288
frameHeight = 720

capLeft = cv2.VideoCapture(2)
capLeft.set(3,frameWidth)
capLeft.set(4,frameHeight)

capRight = cv2.VideoCapture(0)
capRight.set(3,frameWidth)
capRight.set(4,frameHeight)

_, frameLeft = capLeft.read()
_, frameRight = capRight.read()

cv2.namedWindow('Left cam')
cv2.namedWindow('Right cam')
cv2.namedWindow('Depth map')

cv2.createTrackbar('numDIsparities','Depth map',1,10,nothing)
cv2.createTrackbar('blockSize','Depth map',1,10,nothing)


while True:
    _, frameLeft = capLeft.read()
    _, frameRight = capRight.read()

    cv2.imshow('Left cam', frameLeft)
    cv2.imshow('Right cam', frameRight)

    grayLeft = cv2.cvtColor(frameLeft, cv2.COLOR_BGR2GRAY)
    grayRight = cv2.cvtColor(frameRight, cv2.COLOR_BGR2GRAY)


    # cv2.imshow('Left cam', grayLeft)
    # cv2.imshow('Right cam', grayRight)

    # cv2.imwrite( "left.jpg", frameLeft)
    # cv2.imwrite( "right.jpg", frameRight)


    numDisparities = cv2.getTrackbarPos('numDIsparities','Depth map')
    blockSize = cv2.getTrackbarPos('blockSize','Depth map')

    # # print(numDisparities)
    # # print(blockSize)
    # # print(numDisparities*16)
    # # print(blockSize*5)

    stereo = cv2.StereoBM_create(numDisparities=numDisparities*16, blockSize=blockSize*2+5)
    disparity = stereo.compute(grayLeft, grayRight)
    #print(disparity)
    #disparity = cv2.normalize(disparity, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
    # print(disparity[0, 0])
    disparity = disparity.astype(np.uint8)
    #disparity = cv2.cvtColor(disparity, cv2.CV_8UC3)
    cv2.imshow('Depth map', disparity)


    # print(disparity.shape)
    # print(disparity[0, 0])
    # print(disparity[0])

    #disparityColor = cv2.applyColorMap(disparity, cv2.COLORMAP_JET)

    # cv2.imshow('Depth map', disparityColor)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capLeft.release()
capRight.release()
cv2.destroyAllWindows()
