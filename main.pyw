from tkinter import *

def main():
    desenharTela()


def desenharTela():
    window = Tk()
    window.geometry("985x526")
    window.configure(bg = "#ffffff")
    canvas = Canvas(window, bg = "#ffffff", height = 526, width = 985, bd = 0, highlightthickness = 0, relief = "ridge")
    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(0, 0, 0+985, 0+526, fill = "#edd2d2", outline = "")
    canvas.create_rectangle(0, 0, 0+551, 0+526, fill = "#33a7ff", outline = "")
    canvas.create_text(280.5, 174.0, text = "Aplicativo de Reconhecimento Facial", fill = "#fcf7f7", font = ("ArchivoBlack-Regular", 24))
    canvas.create_rectangle(23, 204, 23+520, 204+7,fill = "#fff9f9", outline = "")
    entry0_img = PhotoImage(file = f"imagens_tela/img_textBox0.png")
    #entry0_bg = canvas.create_image(759.5, 246.5,image = entry0_img)
    entry0 = Entry(bd = 0, bg = "#e9e9e9", highlightthickness = 0)
    entry0.place(x = 634, y = 230, width = 251, height = 31)
    entry1_img = PhotoImage(file = f"imagens_tela/img_textBox1.png")
    #entry1_bg = canvas.create_image(759.5, 324.5, image = entry1_img)
    entry1 = Entry(bd = 0, bg = "#e9e9e9", highlightthickness = 0)
    entry1.place( x = 634, y = 308, width = 251, height = 31)
    canvas.create_text( 642.5, 297.5, text = "ID", fill = "#000000", font = ("None", 12))
    canvas.create_text( 656.5, 219.5, text = "Nome", fill = "#000000", font = ("None", 12))
    img0 = PhotoImage(file = f"imagens_tela/img0.png")
    b0 = Button(image = img0, borderwidth = 0, highlightthickness = 0, command = btn_clicked, relief = "flat")
    b0.place(x = 664, y = 404, width = 207, height = 45)
    canvas.create_text(767.5, 138.5, text = "CREDENCIAIS", fill = "#000000", font = ("Roboto-Bold", 24))
    window.resizable(False, False)
    window.mainloop()

def btn_clicked():
    pass


if __name__ == '__main__':
    main()
