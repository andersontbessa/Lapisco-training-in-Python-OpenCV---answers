#A função flatten () ---> é usada para obter uma cópia de um determinado array reduzindo a uma dimensão. Array é matriz. Por exemplo uma matriz bidimencional, vai reduzir para uma matriz unidimensional.
#uint8 --> Inteiros sem sinal de 8 bits. Um tipo de dados uint8 contém todos os números inteiros de 0 a 255. Como acontece com todos os números sem sinal, os valores não devem ser negativos. Uint8 é usado principalmente em gráficos (as cores são sempre não negativas).

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read a rgb image
image = cv2.imread('image.jpg')

# Transform to grayscale
grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Create one vector to contain the original histogram and other to contain the equalized histogram
original_hist = np.zeros([256], np.uint8) #cria uma matriz fazia. obs:Um tipo de dados uint8 contém todos os números inteiros de 0 a 255

equalized_hist = np.zeros([256], np.uint8)
#print (original_hist) #test


# Calculating the initial histogram

img_flat = grayscale_image.flatten() #A função flatten () é usada para obter uma cópia de um determinado array(matriz) reduzindo a uma dimensão.
#print(img_flat)#teste

for pixel in img_flat:
    original_hist[pixel] += 1
#print(original_hist[pixel]) #test
#print(len(original_hist)) #test


# Calculates the cumulative distribution function of the histogram
cdf = [sum(original_hist[:i + 1]) for i in range(len(original_hist))]
cdf = np.array(cdf) #cria uma matriz organizada.

# Normalize the cdf to be between 0-255
normal_cdf = ((cdf - cdf.min())*255)/(cdf.max() - cdf.min())
normal_cdf = normal_cdf.astype('uint8')#o astype('uint8') torna a matriz para uint8.
#print (normal_cdf)#test


equalized_image = normal_cdf[img_flat] #aqui estará um array [252 252 252 ...  60  73  76].
#print("test",equalized_image)#test

equalized_image = np.reshape(equalized_image, grayscale_image.shape) #np.reshape altera a forma da matriz.

plt.figure(1)
plt.subplot(221)
plt.imshow(grayscale_image, cmap='gray')
plt.subplot(222)
plt.hist(grayscale_image.ravel(), 256, [0, 256])
plt.subplot(223)
plt.imshow(equalized_image, cmap='gray')
plt.subplot(224)
plt.hist(equalized_image.ravel(), 256, [0, 256])
plt.show()





