import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Janela principal

janela = tk.Tk()
janela.title("Sistema de Conveniência")
# Dados dos produtos com preços e imagens associadas
produtos = {
    'Vinho': {'preco': 89.90, 'imagem': 'vinho.png'},
    'Garrafa 51': {'preco': 99.99, 'imagem': 'garrafa51.png'},
    'Red Label': {'preco': 70.00, 'imagem': 'redlabel.png'},
    'Jack Daniels': {'preco': 69.00, 'imagem': 'jackdaniels.png'},
    'Refrigerante': {'preco': 10.00, 'imagem': 'refrigerante.png'},
    'Água': {'preco': 6.99, 'imagem': 'agua.png'}
}

# Função para atualizar o total da compra
def atualizar_total():
    total = 0
    for item in carrinho:
        total += produtos[item]['preco'] * carrinho[item]
    total_label.config(text=f'Total: R$ {total:.2f}')

# Função para adicionar um item ao carrinho
def adicionar_ao_carrinho():
    produto_selecionado = bebida_combobox.get()
    quantidade = quantidade_entry.get()

    try:
        quantidade = int(quantidade)
        if produto_selecionado and quantidade > 0:
            if produto_selecionado in carrinho:
                carrinho[produto_selecionado] += quantidade
            else:
                carrinho[produto_selecionado] = quantidade
            mensagem_status.config(text=f'{produto_selecionado} adicionado ao carrinho!', fg="green")
            atualizar_total()
        else:
            raise ValueError
    except ValueError:
        mensagem_status.config(text="Por favor, insira uma quantidade válida!", fg="red")

# Função para exibir a imagem do produto selecionado
def mostrar_imagem():
    produto_selecionado = bebida_combobox.get()
    if produto_selecionado in produtos:
        imagem_produto = produtos[produto_selecionado]['imagem']
        img = tk.PhotoImage(file=imagem_produto)
        label_imagem.config(image=img)
        label_imagem.image = img  # Manter a referência para não perder a imagem

# Função para finalizar a compra
def finalizar_compra():
    if len(carrinho) == 0:
        messagebox.showwarning("Carrinho vazio", "Você não tem itens no carrinho.")
    else:
        total = 0
        resumo_compra = "Resumo da Compra:\n"
        for item, quantidade in carrinho.items():
            preco = produtos[item]['preco'] * quantidade
            total += preco
            resumo_compra += f'{item} x{quantidade} - R$ {preco:.2f}\n'
        resumo_compra += f'\nTotal: R$ {total:.2f}'

        resposta = messagebox.askyesno("Finalizar Compra", f"{resumo_compra}\n\nDeseja finalizar a compra?")
        if resposta:
            carrinho.clear()
            atualizar_total()
            mensagem_status.config(text="Compra finalizada com sucesso!", fg="blue")
        else:
            mensagem_status.config(text="Compra não finalizada.", fg="orange")

# Variáveis
carrinho = {}

# Configuração de Layout
janela.rowconfigure(0, weight=1)
janela.columnconfigure(0, weight=1)

# Labels de Informações
mensagem = tk.Label(janela, text="Sistema de Conveniência", fg='white', bg='#DAA520', width=50, height=2)
mensagem.grid(row=0, column=0, columnspan=2, sticky="NSEW")

# ComboBox para selecionar bebidas
bebida_combobox = ttk.Combobox(janela, values=list(produtos.keys()), state="readonly", width=30)
bebida_combobox.grid(row=1, column=0)
bebida_combobox.bind("<<ComboboxSelected>>", lambda e: mostrar_imagem())  # Chama a função para mostrar imagem

# Entrada para quantidade
quantidade_label = tk.Label(janela, text="Quantidade:")
quantidade_label.grid(row=1, column=1)

quantidade_entry = tk.Entry(janela)
quantidade_entry.grid(row=1, column=2)

# Botão para adicionar ao carrinho
botao_adicionar = tk.Button(janela, text="Adicionar ao Carrinho", command=adicionar_ao_carrinho)
botao_adicionar.grid(row=2, column=0, columnspan=2)

# Exibição do total
total_label = tk.Label(janela, text="Total: R$ 0.00", font=("Arial", 12))
total_label.grid(row=3, column=0, columnspan=2)

# Status da operação (sucesso ou erro)
mensagem_status = tk.Label(janela, text="", fg="red")
mensagem_status.grid(row=4, column=0, columnspan=3)

# Botão para finalizar a compra
botao_finalizar = tk.Button(janela, text="Finalizar Compra", command=finalizar_compra)
botao_finalizar.grid(row=5, column=0, columnspan=3)

# Label para exibir a imagem do produto selecionado
label_imagem = tk.Label(janela)
label_imagem.grid(row=6, column=0, columnspan=3, pady=20)

# Iniciar o loop da janela
janela.mainloop()
