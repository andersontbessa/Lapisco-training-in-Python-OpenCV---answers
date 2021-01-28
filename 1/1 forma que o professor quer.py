import cv2
obj_img = cv2.imread ("paisagem.jpg")

cv2.imshow("image", obj_img)
cv2. waitKey(0)
cv2.imwrite("salv.jpg",obj_img)
