#sobel detecta bordas.
 #Aplicacao do Sobel, Varrendo verticalmente e horizontalmente com as mascaras sobel.
               #Horizontal     Vertical
             #| +1 +2 +1 |    | -1 0 +1 |
             #|  0  0  0 |    | -2 0 +2 |
             #| -1 -2 -1 |    | -1 0 +1 |

                #G=\|Gx^2 + Gy^2 '

import cv2
import numpy as np

# Read a rgb image
image = cv2.imread('image.jpg')

# Transform to grayscale
grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Show the input image
cv2.imshow('Input grayscale image', grayscale_image)

# Get the rows and columns of the image
rows, cols = grayscale_image.shape[:2]

# Create a matrix with the same dimension of the grayscale image
output_image = np.zeros((rows, cols), np.uint8)

# Apply convolution with the Sobel Kernel
for row in range(1, rows-1):
    for col in range(1, cols-1):
        gx = grayscale_image[row - 1, col - 1] * (-1) + grayscale_image[row, col - 1] * (-2) + \
             grayscale_image[row + 1, col - 1] * (-1) + grayscale_image[row - 1, col + 1] + \
             grayscale_image[row, col + 1] * 2 + grayscale_image[row + 1, col + 1]

        gy = grayscale_image[row - 1, col - 1] * (-1) + grayscale_image[row - 1, col] * (-2) + \
             grayscale_image[row - 1, col + 1] * (-1) + grayscale_image[row + 1, col - 1] + \
             grayscale_image[row + 1, col] * 2 + grayscale_image[row - 1, col + 1]

        output_image[row, col] = (gx**2 + gy**2)**(1/2)
#duas vertentes gx e gy na solbel kernel, e calcula no final. #Isso se Operador Sobel.        

# Show the result image
cv2.imshow('Sobel image', output_image)
cv2.waitKey(0)

# Save the result
cv2.imwrite('sobel_result.jpg', output_image)
