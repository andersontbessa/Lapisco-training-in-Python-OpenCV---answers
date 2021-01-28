import numpy as np
import cv2

obj_img = cv2.imread("imgs/paisagem.jpg") #carrega uma imagem

#abre sem todas as tonalidades de cores
from matplotlib import pyplot as plt #flota janelas gráficas. Chama o pyplot dentro de matplotlib
plt.imshow(obj_img)
plt.show() #para a janela gráfica aparecer, tem que chamar o imshow, depois o show.

#ou

#abre com todas as tonalidades de cores
cv2.imshow("imgs/paisagem.jpg",obj_img)
cv2.waitKey(0)





