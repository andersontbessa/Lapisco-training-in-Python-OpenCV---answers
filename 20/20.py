import cv2
import numpy as np
from numba import njit #acelerador


def region_growing(image, seed=None):

    rows, cols = image.shape[:2]

    xc, yc = seed #passa o xc,yc para o seed

    
    segmented = np.zeros_like(image) #cria uma nova matriz em cor de pixel zero.

    segmented[xc, yc] = 255 #aqui centraliza o ponto branco. Passa um ponto branco 255 no meio da imagem
    #print(segmented[xc, yc]) #teste
    current_found = 0
    previous_points = 1

    while previous_points != current_found:

        previous_points = current_found #logo o previous_points passa a ter valor zero como é o current_found
        current_found = 0 #no final o current_found vai resultar em 9, por haver 9 "if".
        for row in range(rows):
            for col in range(cols):
                #aqui se está usando matrix 3x3, por isso se usa apenas -1,1 e +1.
                #lembrar de kernel
                #nos meus downloads tem uma print do raul explicando uma matriz 3x3
                if segmented[row, col] == 255:
                    if image[row - 1, col - 1] < 127: #quando ele achar essa posição -1 e -1, sendo menor que 127, vai acrescentar 255 na mesma posição, e assim vai.
                        segmented[row - 1, col - 1] = 255
                        current_found += 1
                    if image[row - 1, col] < 127:
                        segmented[row - 1, col] = 255
                        current_found += 1
                    if image[row - 1, col + 1] < 127:
                        segmented[row - 1, col + 1] = 255
                        current_found += 1
                    if image[row, col - 1] < 127:
                        segmented[row, col - 1] = 255
                        current_found += 1
                    if image[row, col + 1] < 127:
                        segmented[row, col + 1] = 255
                        current_found += 1
                    if image[row + 1, col - 1] < 127:
                        segmented[row + 1, col - 1] = 255
                        current_found += 1
                    if image[row + 1, col] < 127:
                        segmented[row + 1, col] = 255
                        current_found += 1
                    if image[row + 1, col + 1] < 127:
                        segmented[row + 1, col + 1] = 255
                        current_found += 1 #aparecem 9 "if" porque a matrix é 3x3. Se por exemplo fosse 5x5, iria haver col-2, row-2... etc, iria ter continuidade, mas resultaria na mesma coisa.
                        

    return segmented


if __name__ == '__main__': #esse if serve como inicializador
    image = cv2.imread('image.jpg')

    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#o region_growing é a função acima declarada, e estão passando os parâmetros para dentro dele
    segmented_image = region_growing(grayscale_image,
                                     seed=(int(grayscale_image.shape[0]/2), int(grayscale_image.shape[1]/2)))
                                    #o seed é a semente. Passa o shape metade para cada grayscale.
    cv2.imshow('Segmented image', segmented_image)
    cv2.waitKey(0)

