## imread.py

import numpy as np
import cv2

img = cv2.imread('week13/cb3.png')

#uint8
print(img.dtype)

(3, 2, 3)
print(img.shape)

print(img)



# ## Grayscale
# import numpy as np
# import cv2
#
# # convert image to grayscale
# im_gray = cv2.imread(
#                 'week13/jeanne_small.jpg',
#                 cv2.IMREAD_GRAYSCALE
#             )
#
# # use highgui to display image
# cv2.imshow("Jeanne in Gray", im_gray)
#
# # keeps the image displayed
# cv2.waitKey()