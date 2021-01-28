import cv2
import numpy as np

# Read the .txt file
filename = 'question10_result.txt'
image = []
with open(filename, 'r') as infile:
    # Iterate through lines of the txt file
    for i, line in enumerate(infile):
        # Convert each number of the line to int
        row = [int(number) for number in line.split()]
        #print (line.split()) #só para testar
        #print(row) #só para testar
        # Verify if is the first iteration
        if i == 0:
            # Create the first line of the image
            #o hstack -> Empilhe matrizes em sequência horizontalmente (coluna sábia).
            image = np.hstack(row)
        else:
            
            # If it is not the first iteration, then add new lines to compose the image
            # Empilhar matrizes em sequência verticalmente (linha sábia).
            image = np.vstack(([image, row]))

# Convert the image from float64 to uint8
result = np.asarray(image, np.uint8)

# Show the read image
cv2.imshow('Read image', result)

cv2.waitKey(0)
