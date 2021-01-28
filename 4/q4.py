import numpy as np #flota janelas gráficas. Chama o pyplot dentro de matplotlib

import cv2
from matplotlib import pyplot as plt

obj_img = cv2.imread("imgs/paisagem.jpg", 0)       #carrega uma imagem


obj_img = cv2.cvtColor(obj_img, cv2.COLOR_BGR2RGB) #onde antes era BGR, TRANSFORMA para RGB 
#img = cv2.cvtColor(obj_img, cv2.COLOR_BGR2GRAY)
#print(obj_img.shape)
altura,largura,canais_de_cor = obj_img.shape #o shape serve para a saber a altura, a largura e os canais de cores da foto. Podemos fazer assim separando cada um em uma variável, colocando vírgulas para separar as variáveis.
print("dimensões:",str(altura), "x", str(largura))
print ("canais de cores:",canais_de_cor)

plt.imshow(obj_img)
plt.show()                                      #para a janela gráfica aparecer, tem que chamar o imshow, depois o show.

#cv2.imwrite('pedit.jpg',img)
