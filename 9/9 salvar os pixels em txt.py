import cv2

obj_img = cv2.imread("image.jpg")

img= cv2.cvtColor(obj_img, cv2.COLOR_BGR2GRAY)

cv2.imshow("cinza", img)
cv2.waitKey(0)

#obter linhas e colunas
linhas, colunas = img.shape[:2]

#salvar todos os pixels em um bloco de notas (txt file)
with open ('result.txt', 'w') as outfile:
    for row in range (linhas): #em cada linha, vai percorrer todas as colunas
        for col in range(colunas): 
            outfile.write(str(img[row, col]) + ' ')
        outfile.write('\n')
        
