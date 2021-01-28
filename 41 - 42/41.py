import cv2

image = cv2.imread('image.jpg')

grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

canny_image = cv2.Canny(grayscale_image, 80, 180)

# Create a blob detector
#detector = cv2.SimpleBlobDetector_create()

# Define the parameters
params = cv2.SimpleBlobDetector_Params()

# Filter by Area. #Os blobs extraídos têm uma área entre minArea (inclusive) e maxArea (exclusivo).
params.filterByArea = True
params.minArea = 20
params.maxArea = 40000

# Filter by Circularity #Os blobs extraídos têm circularidade (4 ∗ π∗ A r e ap e r i m e t e r ∗ p e r i m e t e r) entre minCircularity (inclusive) e maxCircularity (exclusivo).
params.filterByCircularity = False
params.minCircularity = 0.1

# Filter by Convexity #Por convexidade . Os blobs extraídos têm convexidade (área / área da casca convexa do blob) entre minConvexity (inclusive) e maxConvexity (exclusivo).

params.filterByConvexity = False
params.minConvexity = 0.87

# Filter by Inertia #Pela proporção da inércia mínima para a inércia máxima . Os blobs extraídos têm essa proporção entre minInertiaRatio (inclusive) e maxInertiaRatio (exclusivo).
params.filterByInertia = False
params.minInertiaRatio = 0.8

# Distance Between Blobs
params.minDistBetweenBlobs = 20

# Create a blob detector with the parameters
detector = cv2.SimpleBlobDetector_create(params)

# Detect objects
blobs = detector.detect(canny_image) #pega a variável acima "detector" ponto detect e passa para o parâmetro a variável com a imagem canny

# Print how many objects are in the image
print(len(blobs)) #tendo em vista a variável "blobs"m onde foi detectado objetos, inserindo-o em um len dá para ver quantos objetos foram detectados.

cv2.imshow('Input grayscale image', grayscale_image)
cv2.waitKey(0)
