import numpy as np
import cv2

img = cv2.imread('redcorn.jpg')
cv2.imwrite("input_test.jpg", img)
height = img.shape[0]
width = img.shape[1]
resized_img = cv2.resize(img,dsize=None, fx=1, fy=1)
cv2.imwrite("input_resized.jpg", resized_img)
bgr = [30,90,230]
thresh = 255
print(resized_img[20,20])

minBGR = np.array([bgr[0] - thresh, bgr[1] - thresh, bgr[2] - thresh])
maxBGR = np.array([bgr[0] + thresh, bgr[1] + thresh, bgr[2] + thresh])

maskBGR = cv2.inRange(resized_img,minBGR,maxBGR)

resultBGR = cv2.bitwise_and(resized_img, resized_img, mask = maskBGR)

#cv2.imshow("Result BGR", resultBGR)
cv2.imwrite("1.jpg", resultBGR)
#cv2.imshow("Result mask", maskBGR)
cv2.imwrite("2.jpg", maskBGR)
for i in range(16):
    x = i * 16
    minBGR = np.array([bgr[0] - x, bgr[1] - x, bgr[2] - x])
    maxBGR = np.array([bgr[0] + x, bgr[1] + x, bgr[2] + x])

    maskBGR = cv2.inRange(resized_img,minBGR,maxBGR)
    cv2.imwrite("range_image_" + str(x) + ".jpg" , maskBGR)

cv2.waitKey(0)
cv2.destroyAllWindows()