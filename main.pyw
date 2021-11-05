from modelos.dadosNivelDois import DadosNivelDois
from modelos.dadosNivelTres import DadosNivelTres
from modelos.dadosNivelUm import DadosNivelUm
from modelos.usuario import Usuario
from reconhecedor_faces.reconhecedor_lbph import reconhecerPessoa
from banco_dados.bd import Bd
from tkinter import *

msgSemAcessoAoDado = 'Sem acesso a esse dado!'
bgColor = "#33a7ff"
textColor = "#ffffff"
labelFont = ("ArchivoBlack-Regular", 12)

window = Tk()
window.geometry("985x526")
window.configure(bg = "#ffffff")
canvas = Canvas(window, bg = "#ffffff", height = 526, width = 985, bd = 0, highlightthickness = 0, relief = "ridge")
canvas.place(x = 0, y = 0)

canvas.create_rectangle(0, 0, 0+985, 0+526, fill = "#edd2d2", outline = "")
canvas.create_rectangle(0, 0, 0+551, 0+526, fill = "#33a7ff", outline = "")
canvas.create_text(280.5, 138.5, text = "Dados obtidos no reconhecimento", fill = "#fcf7f7", font = ("ArchivoBlack-Regular", 24))
canvas.create_rectangle(23, 164, 23+520, 164+7, fill = "#fff9f9", outline = "")

labelNomeProdutora = Label(text="Nome da produtora: ", bg=bgColor, foreground=textColor, font=labelFont)
labelEndereco = Label(text="Endereço: ", bg=bgColor, foreground=textColor, font=labelFont)
labelProduto = Label(text="Produto: ", bg=bgColor, foreground=textColor, font=labelFont)
labelProducao = Label(text="Produção: ", bg=bgColor, foreground=textColor, font=labelFont)
labelDestino = Label(text="Destino: ", bg=bgColor, foreground=textColor, font=labelFont)
labelQtdEmpregados = Label(text="Quantidade de empregados: ", bg=bgColor, foreground=textColor, font=labelFont)
labelQtdMaquinas = Label(text="Quantidade de máquinas: ", bg=bgColor, foreground=textColor, font=labelFont)
labelNivelAutomacao = Label(text="Nível de automação: ", bg=bgColor, foreground=textColor, font=labelFont)

labelIncentivosFiscais = Label(text="Incentivos Fiscais: ", bg=bgColor, foreground=textColor, font=labelFont)
labelimpostosMunicipais = Label(text="Impostos Municipais: ", bg=bgColor, foreground=textColor, font=labelFont)
labelImpostosEstaduais = Label(text="Impostos Estaduais: ", bg=bgColor, foreground=textColor, font=labelFont)
labelImpostosFederais = Label(text="Impostos Federais: ", bg=bgColor, foreground=textColor, font=labelFont)
labelTaxasFederais = Label(text="Taxas Federais: ", bg=bgColor, foreground=textColor, font=labelFont)

labelDescricaoAgrotoxico = Label(text="Agrotóxico utilizado: ", bg=bgColor, foreground=textColor, font=labelFont)

labelNomeProdutora.place(x=20, y=180)
labelEndereco.place(x=20, y=200)
labelProduto.place(x=20, y=220)
labelProducao.place(x=20, y=240)
labelDestino.place(x=20, y=260)
labelQtdEmpregados.place(x=20, y=280)
labelQtdMaquinas.place(x=20, y=300)
labelNivelAutomacao.place(x=20, y=320)

labelIncentivosFiscais.place(x=20, y=360)
labelimpostosMunicipais.place(x=20, y=380)
labelImpostosEstaduais.place(x=20, y=400)
labelImpostosFederais.place(x=20, y=420)
labelTaxasFederais.place(x=20, y=440)

labelDescricaoAgrotoxico.place(x=20, y=480)

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
        dadosNivelUm = None
        dadosNivelDois = None
        dadosNivelTres = None

        nome, nivelAcesso = bd.obterDadosPessoaReconhecida(idPessoaReconhecida)
        usuario = Usuario(idPessoaReconhecida, nome, nivelAcesso)
        textBoxNome.insert(0, usuario.getNome())
        textBoxId.insert(0, usuario.getId())

        if usuario.getNivelAcesso() >= 1:
            dadosNivelUm = DadosNivelUm(bd.obterDadosNivelUm(idProdutora))

        if usuario.getNivelAcesso() >= 2:
            dadosNivelDois = DadosNivelDois(bd.obterDadosNivelDois(idProdutora))

        if usuario.getNivelAcesso() >= 3:
            dadosNivelTres = DadosNivelTres(bd.obterDadosNivelTres(idProdutora))

        if dadosNivelUm != None:
            labelNomeProdutora.config(text=f'Nome da produtora: {dadosNivelUm.getNomeProdutora()}')
            labelEndereco.config(text=f'Endereço: {dadosNivelUm.getEndereco()}')
            labelProduto.config(text=f'Produto: {dadosNivelUm.getProdutos()}')
            labelProducao.config(text=f'Produção: {dadosNivelUm.getProducao()}')
            labelDestino.config(text=f'Destino: {dadosNivelUm.getDestino()}')
            labelQtdEmpregados.config(text=f'Quantidade de empregados: {dadosNivelUm.getQuantiaEmpregados()}')
            labelQtdMaquinas.config(text=f'Quantidade de máquinas: {dadosNivelUm.getQuantidaMaquinas()}')
            labelNivelAutomacao.config(text=f'Nível de automação: {dadosNivelUm.getNivelAutomacao()}')

        if dadosNivelDois != None:
            labelIncentivosFiscais.config(text=f'Incentivos Fiscais: {dadosNivelDois.getIncentivosFiscais()}')
            labelimpostosMunicipais.config(text=f'Impostos Municipais: {dadosNivelDois.getImpostosMunicipais()}')
            labelImpostosEstaduais.config(text=f'Impostos Estaduais: {dadosNivelDois.getImpostosEstaduais()}')
            labelImpostosFederais.config(text=f'Impostos Federais: {dadosNivelDois.getImpostosFederais()}')
            labelTaxasFederais.config(text=f'Taxas Federais: {dadosNivelDois.getTaxasFederais()}')
        else:
            labelIncentivosFiscais.config(text=f'Incentivos Fiscais: {msgSemAcessoAoDado}')
            labelimpostosMunicipais.config(text=f'Impostos Municipais: {msgSemAcessoAoDado}')
            labelImpostosEstaduais.config(text=f'Impostos Estaduais: {msgSemAcessoAoDado}')
            labelImpostosFederais.config(text=f'Impostos Federais: {msgSemAcessoAoDado}')
            labelTaxasFederais.config(text=f'Taxas Federais: {msgSemAcessoAoDado}')

        if dadosNivelTres != None:
            labelDescricaoAgrotoxico.config(text=f'Agrotóxico utilizado: {dadosNivelTres.getDescricaoAgrotoxico()}')
        else:
            labelDescricaoAgrotoxico.config(text=f'Agrotóxico utilizado: {msgSemAcessoAoDado}')

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
