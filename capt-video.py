import cv2
import math

cap = cv2.VideoCapture('videos\p_ball.mp4')
frameRate = cap.get(5)  # frame rate
while (cap.isOpened()):
    frameId = cap.get(1)  # current frame number
    ret, frame = cap.read()
    if (ret != True):
        break
    if frameId % math.floor(frameRate) == 0:
        filename = 'img/image_rec_' + str(int(frameId)) + ".bmp"
        cv2.imwrite(filename, frame)
cap.release()
print ("Done!")