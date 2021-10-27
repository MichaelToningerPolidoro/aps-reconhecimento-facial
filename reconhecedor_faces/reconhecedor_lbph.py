from time import time
import cv2

def obterTempoAtualDoSistemaEmMillisegundos() -> int:
    return int(round(time() * 1000))


def reconhecerPessoa() -> int:
    idPessoaReconhecida = -1
    detectorFace = cv2.CascadeClassifier('reconhecedor_faces/classificadores/haarcascade_frontalface_default.xml')
    reconhecedor = cv2.face.LBPHFaceRecognizer_create()
    reconhecedor.read('reconhecedor_faces/classificadores/classificadorLBPH.yml')
    tempoFinalExecucao = obterTempoAtualDoSistemaEmMillisegundos() + 4500
    camera = cv2.VideoCapture(0)
    
    while True:
        conectado, imagem = camera.read()
        imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
        facesDetectadas = detectorFace.detectMultiScale(imagemCinza, scaleFactor=1.5, minSize=(150, 150))

        for (x, y, largura, altura) in facesDetectadas:
            imagemFace = cv2.resize(imagemCinza[y:y+altura, x:x+largura], (largura, altura))
            idPessoaImagem, confianca = reconhecedor.predict(imagemFace)
            
            if idPessoaReconhecida == -1 and idPessoaImagem > 0:
                idPessoaReconhecida = idPessoaImagem

        cv2.imshow('Face', imagem)
        cv2.waitKey(10)

        if obterTempoAtualDoSistemaEmMillisegundos() > tempoFinalExecucao:
            camera.release()
            cv2.destroyAllWindows()
            break
    
    return idPessoaReconhecida
