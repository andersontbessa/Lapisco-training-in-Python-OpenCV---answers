#momentos de uma imagem --> A técnica de momentos, também chamados momentos estatísticos, é um dos vários métodos utilizados para extração de características de uma imagem. Estes momentos e as funções derivadas deles se caracterizam por valores numéricos calculados a partir da imagem previamente segmentada e que descrevem a distribuição espacial dos pontos contidos na imagem ou em uma região.

#GLOB--> Mas, poderíamos querer listar somente os arquivos .py, por exemplo, para abrí-los, em sequência. É aí que entra o módulo glob. Ele permite que listemos os arquivos de um diretório, usando expressões semelhantes as que usamos no shell, como por exemplo: *.py.
#ou seja, serve para listar arquivos de um diretório




import cv2
import os
import glob
import csv


def extract_spatial_moments(images):
    print('[INFO] Extracting spatial moments.')
    spatial_moments = []

    for i, image in enumerate(images):
         # Load the rgb image
        file = cv2.imread(image)

        # Convert to grayscale
        file = cv2.cvtColor(file, cv2.COLOR_BGR2GRAY)

        print('[INFO] Extracting features of image {}/{}'.format(i + 1, len(images)))
        

        # Extract the moments
        moments = cv2.moments(file)

        # Create a list with the features extracted
        spatial_moments.append([moments['m00'], moments['m10'], moments['m01'], moments['m20'], moments['m11'],
                                moments['m02'], moments['m30'], moments['m21'], moments['m12'], moments['m03']])

    print('\n')

    return spatial_moments


def save_results(extractor_name, features):

    # Show the extracted features in command prompt
    for vector in features:
       print(vector)
        

    # Save all features in a csv file
    with open(extractor_name + '.csv', 'w') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(features) #salva o que estava em features dentro de um arquivo de excel


if __name__ == '__main__':

    # Inform the path to the rgb images
    # Informe o caminho para as imagens rgb

    dataset = 'dataset/'

    # Grab all the paths to the images with extension .jpg
    # Pegue todos os caminhos para as imagens com extensão .jpg

    image_paths = glob.glob(os.path.join(dataset, '*.jpg')) #aqui vai estar todas as imagens com suas descrições que estão nomeados dentra da pasta dataset

    # Extract Spatial Moments # Extraia momentos espaciais 
    features = extract_spatial_moments(image_paths) #a função extract_spatial_moments que está lá em cima vai receber a image_paths das 11 imagens. 


    # Save the results in a csv file.
    save_results('SpatialMoments', features)#dai os valores
