import cv2
import numpy as np
import random

image = cv2.imread('image.jpg')

grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

canny_image = cv2.Canny(grayscale_image, 80, 180)

# Define the parameters
params = cv2.SimpleBlobDetector_Params()

# Filter by Area.
params.filterByArea = True
params.minArea = 20
params.maxArea = 40000

# Filter by Circularity
params.filterByCircularity = False
params.minCircularity = 0.1

# Filter by Convexity
params.filterByConvexity = False
params.minConvexity = 0.87

# Filter by Inertia
params.filterByInertia = False
params.minInertiaRatio = 0.8

# Distance Between Blobs
params.minDistBetweenBlobs = 20

# Create a blob detector with the parameters
detector = cv2.SimpleBlobDetector_create(params)

# Detect objects
blobs = detector.detect(canny_image)

# Print how many objects are in the image
print(len(blobs))

rows, cols = image.shape[:2]
print ("os valores máximos da matriz da imagem são",[rows, cols])#teste

# Draw blobs
for i, k in enumerate(blobs): 
    print ("valores de", k) #quando a gente printa vai retornar um keypoint, e nele virá as coodenadas x e y,assim como outras informações

    # Get the coordinates of up_left and bottom_right
    x_up_left = int(k.pt[0] - k.size) #keypoint carrega primeiro x e y, exemplo "keypoint=[214 2000]". Provavelmente o k.pt[0] é o x e o "k.pt[1]" é o y. 
    y_up_left = int(k.pt[1] - k.size) #no caso o up_left vai para o lado esquerdo e o bottom_right vai para o lado direito
    print (k.pt[0])#teste
    print (k.pt[1])#teste
    print (k.size)#teste
    
    x_bottom_right = int(k.pt[0] + k.size) #keypoint carrega primeiro x e y, exemplo "keypoint=[214 2000]". Provavelmente o k.pt[0] é o x e o "k.pt[1]" é o y. 
    y_bottom_right = int(k.pt[1] + k.size) #no caso o up_left vai para o lado esquerdo e o bottom_right vai para o lado direito

    # Verify if this coordinates are inside the limits of the image, correct if it is not inside the limits
    if x_up_left < 0: #se a coordenada x for menor do que o plano cartesiano, vai receber zero, que é o limite do plano cartesiano.
        x_up_left = 0
    if y_up_left < 0: #se a coordenada y for menor do que o plano cartesiano, vai receber zero, que é o limite do plano cartesiano.
        y_up_left = 0

    if x_bottom_right > cols:   #como o shape[:2] retorna os valores máximos de x e y da matriz da imagem, se as coordenadas de x bottom_right e y bottom_right passar do valor máximo da matriz da imagem, esses vão receber o valor máximo que onde a matriz da imagem.
        x_bottom_right = cols
    if y_bottom_right > rows:
        y_bottom_right = rows

    # # Draw the rectangle
    # cv2.rectangle(image, (x_up_left + 15, y_up_left + 15), (x_bottom_right - 15, y_bottom_right - 15), (255, 0, 0), 2)

    #    each object
    crop = image[y_up_left + 15:y_bottom_right - 15, x_up_left + 15:x_bottom_right - 15] #aqui vai ser o corte. Eu regulo onde será cortada tendo em vista os valores das coordenadas de y e x.

    # Show the objects
    cv2.imshow('Object ' + str(i + 1), crop)
    cv2.waitKey(10)


# Show the input image
cv2.imshow('Input grayscale image', grayscale_image)
cv2.waitKey(0)
