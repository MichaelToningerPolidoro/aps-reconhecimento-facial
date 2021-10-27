import cv2
import numpy as np

classificador = cv2.CascadeClassifier('reconhecedor_faces/classificadores/haarcascade_frontalface_default.xml')
classificadorOlho = cv2.CascadeClassifier('reconhecedor_faces/classificadores/haarcascade_eye.xml')

camera = cv2.VideoCapture(0)
caminhoImagens = 'reconhecedor_faces/fotos'
amostra = 1
numeroDeAmostras = 25
larguraImagem = 220
alturaImagem = 220
corQuadradoVermelho = (0, 0, 255)
corQuadradoVerde = (0, 255, 0)
borda = 2
nivelLuminosidadeBoa = 110

#Id para reconhecer quem é a pessoa, ou seja, identificador pode ser o nome
id = input('Digite seu identificador: ')
print('Capturando as faces ...')

while True:
    conectado, imagem = camera.read()
    imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    facesDetectadas = classificador.detectMultiScale(imagemCinza, scaleFactor=1.5, minSize=(150, 150))
    
    for (x, y, largura, altura) in facesDetectadas:
        cv2.rectangle(imagem, (x, y), (x + largura, y + altura), corQuadradoVermelho, borda)
        regiao = imagem[y:y+altura, x:x+largura]
        regiaoCinzaOlho = cv2.cvtColor(regiao, cv2.COLOR_BGR2GRAY)
        olhosDetectados = classificadorOlho.detectMultiScale(regiaoCinzaOlho)

        for (olhox, olhoy, olhoLargura, olhoAltura) in olhosDetectados:
            cv2.rectangle(regiao, (olhox, olhoy), (olhox+olhoLargura, olhoy+olhoAltura), corQuadradoVerde, borda)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                if np.average(imagemCinza) > nivelLuminosidadeBoa:
                    imagemFace = cv2.resize(imagemCinza[y:y+altura, x:x+largura], (largura, altura))
                    cv2.imwrite(f'{caminhoImagens}/pessoa.{id}.{amostra}.jpg', imagemFace)
                    print(f'Foto {amostra} capturada com sucesso')
                    amostra += 1

    cv2.imshow("Face", imagem)
    cv2.waitKey(1)

    if (amostra >= numeroDeAmostras + 1):
        break

print('Faces capturadas com sucesso')
camera.release()
cv2.destroyAllWindows()