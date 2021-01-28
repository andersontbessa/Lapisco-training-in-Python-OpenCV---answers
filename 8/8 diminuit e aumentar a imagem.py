#cv2.resize --> pega as linhas e coluna da matriz e aumenta


import cv2
image = cv2.imread('imgs/paisagem.jpg')

img = cv2.cvtColor (image, cv2.COLOR_BGR2GRAY)

linhas, colunas= img.shape[:2]

#aumenta o dobro da imagem
double=cv2.resize(img, (int(2 * linhas),int(2 * colunas)))

#diminui a metade da imagem
half=cv2.resize(img, (int(linhas/2), int(colunas/2)))


cv2.imshow ('double sized', double)
cv2.imshow ('half sized', half)


cv2.waitKey(0)

cv2.imwrite('double sized.jpg',double)
cv2.imwrite('half sized.jpg',half)
