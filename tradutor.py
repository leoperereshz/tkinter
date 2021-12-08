#pip install pygubu-designer
#pip install googletrans==3.1.0a0 #outras versões dá pau
#pip install ttkthemes
#pip install ttkbootstrap

from tkinter import Tk, ttk, Text
from ttkthemes import ThemedTk
from googletrans import Translator
from ttkbootstrap import Style

def traduzir(evento = None):
    texto = entrada.get('1.0', 'end') #pega da 1a linha, posição zero, até o fim
    src= combo_entrada.get()
    dest = combo_saida.get()
    resultado = translator.translate(text=texto, src=src, dest=dest)
    
    saida.configure(state='normal')
    saida.delete('1.0','end') #limpa da 1a linha, posição zero até o fim
    saida.insert('1.0', resultado.text)
    saida.configure(state='disabled')


values = [ 'pt', 'es', 'en']
translator = Translator()

#janela = Tk()
#janela = ThemedTk(theme='equilux')

style = Style(theme='pulse')
janela = style.master

janela.title('Traduza com dunossauro')

frame_geral = ttk.Frame()

frame_entrada = ttk.Frame(frame_geral)
label_entrada = ttk.Label(frame_entrada,text="Entrada",font=('Arial',14))
combo_entrada = ttk.Combobox(frame_entrada,values=values, font=('Arial',14))
combo_entrada.set('pt')

label_entrada.grid(row=0, column=0, padx=10, pady=10)
combo_entrada.grid(row=0, column=1, padx=10, pady=10)
frame_entrada.pack()

entrada = Text(frame_geral, height=10, width=50)
entrada.pack(padx=10, pady=5, fill='both', expand='yes')

frame_saida = ttk.Frame(frame_geral)
label_saida = ttk.Label(frame_saida,text="Saída", font=('Arial',14))
combo_saida = ttk.Combobox(frame_saida,values=values, font=('Arial',14))
combo_saida.set('en')

label_saida.grid(row=0, column=0, padx=10, pady=5)
combo_saida.grid(row=0, column=1, padx=10, pady=5)
frame_saida.pack()

botao = ttk.Button(frame_geral,text='Traduzir', command=traduzir)
botao.pack(fill='both', padx=10, pady=5)

saida = Text(frame_geral,height=10, width=50, state='disabled')
saida.pack(padx=10, pady=5, fill='both', expand='yes')

frame_geral.pack()

janela.bind('<Return>', traduzir)

janela.mainloop()
