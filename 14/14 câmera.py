import cv2
#chama a câmera
cap = cv2.VideoCapture(0)

while 1:
    ret, frame=cap.read()

    #transforma o vídeo para cinza
    grayscale_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #para aparecer a câmera com imagens
    cv2.imshow('video', grayscale_image)

    #se apertar 'q' a câmera pausa
    if cv2.waitKey(1) & 0xFF == ord('q'):
    #if cv2.waitKey(1) == 27: #Dessa forma, se apertar o ESQ o vídeo pausa
        break



    
