import numpy as np
import time,uuid
import cv2

img_src = "d:/imgWork/1.png";
dest_name = str(uuid.uuid1());
dest_name = "dest";
img_dest = "d:/imgWork/" + dest_name + ".png";
R = 10

img = cv2.imread(img_src)

edges = cv2.Canny(img, 50, 100)
cv2.imwrite(img_dest, edges)
# time.sleep(1)

#获取圆形
# circles1 = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, 2, 400,param1=100, param2=50, minRadius=R-1, maxRadius=R+1)
# # 取出第一个圆
# circles = circles1[0]
# # 转化为uint16类型
# circles = np.uint16(np.around(circles))
# print(circles[0])

#标记边缘
img = cv2.imread(img_dest)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

binary,contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours, -1, (0, 0, 255), 3)

#画圆
radius = 20;
# cv2.circle(img, (0, 100), radius, (0, 255, 0), -1)

lvl = len(contours)-320;
lvl2 = len(contours[lvl])-1

arr = contours[lvl];
lvlPoint = contours[lvl][3][0]
cv2.circle(img, (lvlPoint[0], lvlPoint[1]), radius, (0, 255, 0), -1)

cv2.imwrite(img_dest, img)

# cv2.imshow("img", img)
# cv2.waitKey(0)