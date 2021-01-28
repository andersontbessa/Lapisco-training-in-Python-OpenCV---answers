import cv2
import os
import glob
import csv


def extract_central_moments(images):
    print('[INFO] Extracting central moments.')
    central_moments = []

    for i, image in enumerate(images):

        print('[INFO] Extracting features of image {}/{}'.format(i + 1, len(images))) #o len(images) vai pegar as strings das imagens e contar, que serão 11.
        #print('só teste', len(images))#só teste


        # Load the rgb image
        file = cv2.imread(image)
        #print (image) #só teste
        #cv2.imshow('image', file) # para caso queira que apareça o conjunto das imagens que foram armazenadas em image, que é a variável image_paths.
        #cv2.waitKey(0)

        # Convert to grayscale
        file = cv2.cvtColor(file, cv2.COLOR_BGR2GRAY)

        # Extract the moments
        moments = cv2.moments(file)

        # Create a list with the features extracted
        central_moments.append([moments['mu20'], moments['mu11'], moments['mu02'], moments['mu30'], #a mudança do código da questão 46 foram esse "mu" algum número, sendo os números diferentes.
                                moments['mu21'], moments['mu12'], moments['mu03']])
    print('\n')
    #print('centravush',central_moments) #tsst

    return central_moments



def save_results(extractor_name, features):

    # Show the extracted features in command prompt
    for vector in features:
        print(vector)

    # Save all features in a csv file
    with open(extractor_name + '.csv', 'w') as outfile:
        writer = csv.writer(outfile)  #o csv separa os elementos em vírgular e joga no excel. Essa vírgulas justamente separa os elementos lá no excel para organzar.
        writer.writerows(features)


if __name__ == '__main__':

    # Inform the path to the rgb images
    dataset = 'dataset/'

    # Grab all the paths to the images with extension .jpg
    image_paths = glob.glob(os.path.join(dataset, '*.jpg')) #aqui forma uma lista com todos os caminhos das imagens
    #print('teste', image_paths)#teste

    # Extract central Moments
    features = extract_central_moments(image_paths) #o fectures vai armazenar o  return central_moments dessa função, que é o retorno da função
    #print ("testeando", features)#teste4
    


    # Save the results in a csv file.
    save_results('CentralMoments', features) #como o features está recebendo a função extract_central_moments(image_paths), aqui será retorna o  return central_moments em features.
