import tkinter as tk

janela = tk.Tk()

janela.title("Cotação de moedas")
mensagem = tk.Label(text="Sistema de Busca de Cotação de Moedas", fg='white', bg='#7E40C8', width=50, height=10)
mensagem.pack()

mensagem2 = tk.Label(text = " Selecione a moeda desejada", height=15, width=70)
mensagem2.pack()

moeda = tk.Entry()
moeda.pack()
    
janela.mainloop()