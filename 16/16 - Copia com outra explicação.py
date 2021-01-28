import cv2
import numpy as np
import matplotlib.pyplot as plt

obj_img = cv2.imread("image.jpg")
plt.hist(obj_img.ravel(), 256, [0, 256])#o ravel pega a matrix 2D e linha a linha vai combinar essa linhas para formar um vetor de uma dimensão só.
#[0, 256] quer dizer que o histograma começa em zero e termina em 256. É o intervalo do histograma
cv2.imshow("imagem orig", obj_img)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

