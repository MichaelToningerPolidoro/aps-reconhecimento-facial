from modelos.usuario import Usuario
from reconhecedor_faces.reconhecedor_lbph import reconhecerPessoa
from banco_dados.bd import Bd
from tkinter import *

window = Tk()
window.geometry("985x526")
window.configure(bg = "#ffffff")
canvas = Canvas(window, bg = "#ffffff", height = 526, width = 985, bd = 0, highlightthickness = 0, relief = "ridge")
canvas.place(x = 0, y = 0)
canvas.create_rectangle(0, 0, 0+985, 0+526, fill = "#edd2d2", outline = "")
canvas.create_rectangle(0, 0, 0+551, 0+526, fill = "#33a7ff", outline = "")
canvas.create_text(280.5, 138.5, text = "Dados obtidos no reconhecimento", fill = "#fcf7f7", font = ("ArchivoBlack-Regular", 24))
canvas.create_rectangle(23, 164, 23+520, 164+7, fill = "#fff9f9", outline = "")
textBoxNome = Entry(bd = 0, bg = "#e9e9e9", highlightthickness = 0)
textBoxNome.place(x = 634, y = 230, width = 251, height = 31)
textBoxId = Entry(bd = 0, bg = "#e9e9e9", highlightthickness = 0)
textBoxId.place(x = 634, y = 308, width = 251, height = 31)
canvas.create_text(642.5, 297.5, text = "ID", fill = "#000000", font = ("None", 12))
canvas.create_text(656.5, 219.5, text = "Nome", fill = "#000000", font = ("None", 12))
img0 = PhotoImage(file = f"imagens_tela/img0.png")
canvas.create_text(767.5, 138.5, text = "Dados Pessoa Reconhecida", fill = "#000000", font = ("Roboto-Bold", 20))
window.resizable(False, False)
bd = Bd()

def abrirTela():
    b0 = Button(image = img0, borderwidth = 0, highlightthickness = 0, command = obterDados, relief = "flat")
    b0.place(x = 664, y = 404, width = 207, height = 45)
    window.mainloop()

#Esse Id da produtora ainda é fixo, pois o projeto é apenas um protótipo
def obterDados(idProdutora = 1):
    idPessoaReconhecida = reconhecerPessoa()
    limparTodosOsCamposContendoDados()
    
    if idPessoaReconhecida != -1:
        nomeProdutora = endereco = produtos = producao = destino = qtdEmpregados = qtdMaquinas = nivelAutomacao = None
        incentivosFiscais = impostosMunicipais = impostosEstaduais = impostosFederais = taxasFederais = None
        descricaoAgrotoxico = None
        nome, nivelAcesso = bd.obterDadosPessoaReconhecida(idPessoaReconhecida)
        usuario = Usuario(idPessoaReconhecida, nome, nivelAcesso)
        textBoxNome.insert(0, usuario.getNome())
        textBoxId.insert(0, usuario.getId())

        if usuario.getNivelAcesso() >= 1:
            nomeProdutora, endereco, produtos, producao, destino, qtdEmpregados, qtdMaquinas, nivelAutomacao = bd.obterDadosNivelUm(idProdutora)

        if usuario.getNivelAcesso() >= 2:
            incentivosFiscais, impostosMunicipais, impostosEstaduais, impostosFederais, taxasFederais = bd.obterDadosNivelDois(idProdutora)

        if usuario.getNivelAcesso() >= 3:
            descricaoAgrotoxico = bd.obterDadosNivelTres(idProdutora)[0]

    else:
        mensagem = 'Pessoa não registrada!'
        textBoxNome.insert(0, mensagem)
        textBoxId.insert(0, mensagem)


def limparTodosOsCamposContendoDados():
    textBoxNome.delete(0, len(textBoxNome.get()))
    textBoxId.delete(0, len(textBoxId.get()))


def conectarComBancoDeDados():
    bd.conectarBd()


def main():
    conectarComBancoDeDados()
    abrirTela()


if __name__ == '__main__':
    main()
