import numpy as np
import cv2
import os

#Parametros treshold -> quanto menor mais parecidas precisam ser as imagens, num_components, quantia
#de componentes da face utilizados para reconhecer alguem ou algo (PCA)
#eigenface = cv2.face.EigenFaceRecognizer_create()
#fisherface = cv2.face.FisherFaceRecognizer_create()
lbph = cv2.face.LBPHFaceRecognizer_create()
caminho_imagens = 'reconhecedor_faces/fotos'

def getImagemComId():
    caminhos = [os.path.join(caminho_imagens, f) for f in os.listdir(caminho_imagens)]
    faces = []
    ids = []

    for caminhoImagem in caminhos:
        imagemFace = cv2.cvtColor(cv2.imread(caminhoImagem), cv2.COLOR_BGR2GRAY)
        id = int(os.path.split(caminhoImagem)[-1].split('.')[1])

        ids.append(id)
        faces.append(imagemFace)

    return np.array(ids), faces


ids, faces = getImagemComId()

print('Treinando ...')

#Aprendizagem supervisionada, pois passa junto com os IDS
#eigenface.train(faces, ids)
#eigenface.write('classificadorEigen.yml')

#fisherface.train(faces, ids)
#fisherface.write('classificadorFisher.yml')

lbph.train(faces, ids)
lbph.write('classificadorLBPH.yml')

print('Treinamento realizado !!!')
