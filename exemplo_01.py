from tkinter import Tk, Label, Button

def fui_clicado():
    print('Fui clicado')
    botao.config(text= "Fui clicado!")

def muda_label(evento):
    print("Apertei 1?")
    texto.config(text="Apertei 1?")

janela = Tk()

texto = Label(text="Olá live de Python", font=('Arial',18))
texto.pack()

text2 = Label(text="Live de Python")
text2.pack()

botao = Button(text = "Clicar", font=("Arial", 50), command=fui_clicado)
botao.pack()

janela.bind('1', muda_label)

janela.mainloop()
