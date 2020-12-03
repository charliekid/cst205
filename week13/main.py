# CST 205
# Charlie Nguyen
# 11/17/20
# I was messing around with the video part and the changing of the color.

# ## Grayscale
# import numpy as np
# import cv2
#
# # convert image to grayscale
# im_gray = cv2.imread(
#                 'jeanne_small.jpg',
#                 cv2.IMREAD_GRAYSCALE
#             )
#
# # use highgui to display image
# cv2.imshow("Jeanne in Gray", im_gray)
#
# # keeps the image displayed
# cv2.waitKey()

### Video capture
import numpy as np
import cv2

my_video = cv2.VideoCapture('woman_reading.mp4')

frame_rate = my_video.get(cv2.CAP_PROP_FPS)

wait_value = int(1000/frame_rate)

while True:
    ret, frame = my_video.read()

    if ret:
        # CIE XYZ color space
        cie_xyz = cv2.cvtColor(frame, cv2.COLOR_BGR2XYZ)
        #cie_xyz = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        cv2.imshow('woman reading', cie_xyz)
        cv2.waitKey(wait_value)
    else:
        break

# import cv2
# img = cv2.imread('jeanne_small.jpg')
#
# cv2.rectangle(
#     img,
#     (185, 254),
#     (265, 334),
#     (0, 255, 0),
#     2
#
# )
#
# cv2.imshow("Rectangled", img)
# cv2.waitKey()