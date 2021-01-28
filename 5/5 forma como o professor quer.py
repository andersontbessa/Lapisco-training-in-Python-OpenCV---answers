import cv2

#seleciona a imagem
obj_img = cv2.imread ("imgs/paisagem.jpg")

#cor da imagem cinza
img=cv2.cvtColor(obj_img, cv2.COLOR_BGR2GRAY)

#median e blur em duas variáveis
median_image = cv2.medianBlur(img, ksize=5)
blur_image = cv2.blur(img, ksize=(5,5))

#roda a imagem
cv2.imshow("gray_image", img)
cv2.imshow("median", median_image)
cv2.imshow("blur", blur_image)
cv2.waitKey(0)

#salva a imagem
cv2.imwrite("salvo_n4.jpg", img)
cv2.imwrite("salvo_n5.jpg", median_image)
cv2.imwrite("salvo_n6.jpg", blur_image)



