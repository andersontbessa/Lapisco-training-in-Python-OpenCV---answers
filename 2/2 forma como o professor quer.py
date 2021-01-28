
import cv2
obj_img = cv2.imread ("imgs/paisagem.jpg")

img= cv2.cvtColor(obj_img, cv2.COLOR_BGR2GRAY)


cv2.imshow("image", img)
cv2.waitKey(0)
cv2.imwrite("salv2.jpg",img)
