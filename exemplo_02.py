from tkinter import Tk, ttk, Button

#TTK
#www.pythontutorial.net/tkinter/ttk-stype

janela = Tk()
estilo = ttk.Style()
estilo.configure(
    "TButton",
    font=("Arial", 18)
)

b1 = Button(text="Live de Python")
b2 = ttk.Button(text="Live de Python")

#print(b1.winfo_class()) #Button
#print(b2.winfo_class()) #TButtion

b1.pack()
b2.pack(padx=15, pady=15) #padding

janela.mainloop()

