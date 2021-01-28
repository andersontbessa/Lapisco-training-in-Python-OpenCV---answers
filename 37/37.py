#Criamos manualmente elementos de estruturação nos exemplos anteriores com a ajuda do Numpy. É uma forma retangular. Mas, em alguns casos, você pode precisar de grãos de formato elíptico / circular. Portanto, para este propósito, OpenCV possui uma função, cv2.getStructuringElement () . Basta passar a forma e o tamanho do kernel, você obtém o kernel desejado.
import cv2

image = cv2.imread('image.jpg')

grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow('Input grayscale image', grayscale_image)

ret, threshold_image = cv2.threshold(grayscale_image, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

cv2.imshow('Threshold image', threshold_image)

# cria um Elemento Estruturante
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 3)) #o MORPH_RECT é para ir deixando a imagem branca retangular.
                                                            #o MORPH_ELLIPSE é em forma eliptica.
                                                            #o MORPH_CROSS é em formato de cruz.
                                                            #o (1, 3) regula se mais para vertical ou lateral

# Apply the dilation
for i in range(9):
    dilation = cv2.dilate(threshold_image, kernel, iterations=i)

    # Show the result of the dilation
    cv2.imshow('Dilated image', dilation)
    cv2.waitKey(1000)
