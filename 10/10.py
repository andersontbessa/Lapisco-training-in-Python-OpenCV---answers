import cv2
import numpy as np

obj_img = cv2.imread("imgs/paisagem.jpg")

img = cv2.cvtColor(obj_img, cv2.COLOR_BGR2GRAY)

cv2.imshow('cinza', img)
cv2.waitKey (0)

rows, cols = img.shape[:2] #pega a linha e coluna máxima
#print([rows,cols]) #teste


threshold_matrix = np.zeros((rows, cols), dtype=np.uint8) # para uma cópia da matrix da imagem

for row in range(rows):
    for col in range(cols):
        threshold_matrix[row,col]= img[row, col]
        #print([row,col])#teste
        #print (threshold_matrix[row,col]) #teste
        #print([row,col]) #teste
        #print (img[row, col]) #teste


with open('result.txt', 'w') as outfile:
    for row in range(rows):
        for col in range(cols):
            
            if threshold_matrix[row, col] < 127:
                threshold_matrix[row, col] = 0
            else:
                threshold_matrix[row, col] = 255

            outfile.write(str(threshold_matrix[row, col]) + ' ')
        outfile.write('\n')

