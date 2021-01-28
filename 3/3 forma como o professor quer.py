import cv2
obj_img = cv2.imread ("imgs/paisagem.jpg")

blue_channel, green_channel, red_channel = cv2.split(obj_img)


cv2.imshow('Blue Channel', blue_channel)
cv2.imshow('Green Channel', green_channel)
cv2.imshow('Red Channel', red_channel)

cv2. waitKey(0)
cv2.imwrite("salva_blue.jpg",blue_channel)
cv2.imwrite("salva_green.jpg",green_channel)
cv2.imwrite("salva_red.jpg",red_channel)
