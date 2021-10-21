import cv2

idPessoaReconhecida = -1
detectorFace = cv2.CascadeClassifier('reconhecedor_faces/haarcascade_frontalface_default.xml')
reconhecedor = cv2.face.LBPHFaceRecognizer_create()
reconhecedor.read('reconhecedor_faces/classificadorLBPH.yml')
largura, algura = 220, 220
cor = (0, 0, 255)
borda = 2
font = cv2.FONT_HERSHEY_COMPLEX_SMALL
tamanhoFont = 2
camera = cv2.VideoCapture(0)

while True:
    conectado, imagem = camera.read()
    imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    facesDetectadas = detectorFace.detectMultiScale(imagemCinza, scaleFactor=1.5, minSize=(150, 150))

    for (x, y, largura, altura) in facesDetectadas:
        imagemFace = cv2.resize(imagemCinza[y:y+altura, x:x+largura], (largura, altura))
        pontoInicial, pontoFinal = (x, y), (x+largura, y+altura)
        cv2.rectangle(imagem, pontoInicial, pontoFinal, cor, borda)
        #Esse id abaixo que obtem qual pessoa reconheceu
        idPessoaReconhecida, confianca = reconhecedor.predict(imagemFace)
        cv2.putText(imagem, str(idPessoaReconhecida), (x, y+(altura+30)), font, tamanhoFont, cor)


    cv2.imshow('Face', imagem)

    #if (idPessoaReconhecida != -1):
        #break

    if cv2.waitKey(1) == ord('q'):
        break


camera.release()
cv2.destroyAllWindows()

print('A pessoa reconhecida foi: ' + str(idPessoaReconhecida))
