import cv2
import numpy as np
from numba import njit

seed = (0, 0)


@njit
def region_growing(image, seed=None):

    rows, cols = image.shape[:2]

    xc, yc = seed
    #print(seed)#teste #aqui o xc,yc vai receber o (0,0) do seed lá de cima. Cada um vai ficar com valor zero.
    #print(yc)#teste
    segmented = np.zeros_like(image)

    segmented[xc, yc] = 255

    current_found = 0
    previous_points = 1

    while previous_points != current_found:

        previous_points = current_found
        current_found = 0
        for row in range(rows):
            for col in range(cols):
                if segmented[row, col] == 255:
                    if image[row - 1, col - 1] < 127:
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
                   

    return segmented

#para mexer na imagem com o mouse.
def mouse_event(event, x, y, flags, param): #os x e y são as dimensões na matriz. #o flags e params não precisa usar.
    global seed #chama o seed lá de cima.
    if event == cv2.EVENT_LBUTTONDOWN:  #EVENT_LBUTTONDOWN significa que vai ser com um click. Existe o double click em outro.
        

        seed = (y, x) #o seed vai receber os valores de x, y que estão como parâmetro, que são as dimensões da matriz da imagem.
        print (seed)#ou (y,x)) #nesse print eu enxergo as dimensões ao clicar na imagem. (foi eu que coloquei)
        


if __name__ == '__main__':
    image = cv2.imread('image.jpg')

    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    cv2.namedWindow('Original Image', 1)#abre uma tela
    cv2.imshow('Original Image', grayscale_image)
    cv2.setMouseCallback('Original Image', mouse_event) #são os clicks
    cv2.waitKey(0)

    segmented_image = region_growing(grayscale_image, seed)

    cv2.imshow('Segmented image', segmented_image)
    cv2.waitKey(0)
