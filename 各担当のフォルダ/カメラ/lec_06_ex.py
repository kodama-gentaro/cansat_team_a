import numpy as np
import cv2
from PIL import Image
import os

def resize(scale,image):
    image_resized = cv2.resize(image, dsize=None, fx=scale, fy=scale)
    return image_resized

def RGBtoScore(image , A, B, C):
    r=np.array(image[:,:,2],dtype=np.int64)
    g=np.array(image[:,:,1],dtype=np.int64)
    b=np.array(image[:,:,0],dtype=np.int64)
    image_converted=((r*A-b*B-g*C)+255*(B+C))//(A+B+C)
    print(image_converted)
    print(image_converted[20,20])
    image_converted=np.array(image_converted,dtype=np.uint8)
    return image_converted

def binarization(image):
    th,image_binarizated=cv2.threshold(image, 0, 255, cv2.THRESH_OTSU)
    return th,image_binarizated

def findcorn(scale,image):
    corn=np.zeros(2)
    n,m=image.shape
    num_found = 0
    sum_x = 0
    sum_y = 0
    for i in range(n):
        for j in range(m):
            if(image[i,j]==255):
                corn=([i,j])
                sum_x += i
                sum_y += j
                num_found += 1
    corn[1] = sum_x // num_found
    corn[0] = sum_y // num_found
    scale=int(1/scale)
    corn[0]=scale*corn[0]
    corn[1]=scale*corn[1]
    return corn

def pointcorn(x,y,image,th):
    image=cv2.circle(image, (x, y), 5, (255, 255, 255), thickness=2)
    image = cv2.putText(image, str(th), (0, 50), cv2.FONT_HERSHEY_PLAIN, 4, (0, 255, 0), 5, cv2.LINE_AA)
    return image
def write_notfound(image,th):
    image = cv2.putText(image, "NotFound"+str(th), (0, 50), cv2.FONT_HERSHEY_PLAIN, 4, (0, 255, 0), 5, cv2.LINE_AA)
    return image
file_list = os.listdir("images_from_internet")
print(file_list)
for file in file_list:
    original_image =cv2.imread("images_from_internet/" + file)
    scale=1
    image=resize(scale,original_image)
    image=RGBtoScore(image, 15, 5, 10)
    cv2.imwrite("images/outputs/output" + file + "gray.jpg",image)
    #cv2.imwrite("images/outputs/togray.jpg",image)
    th,image=binarization(image)
    cv2.imwrite("images/outputs/output" + file + "bi.jpg",image)
    if th > 145:
        x,y = findcorn(scale,image)
        image=pointcorn(x,y,original_image,th)
    else:
        image=write_notfound(original_image,th)
    cv2.imwrite("images/outputs/output" + file + ".jpg",image)





