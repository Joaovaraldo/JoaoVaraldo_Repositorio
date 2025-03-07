import tkinter as tk

from PIL import Image, ImageTk
import os

def mostrar_imagem(produto_selecionado):
    if produto_selecionado in produtos:
        imagem_produto = produtos[produto_selecionado]['imagem']
        
        # Verificando se o arquivo da imagem existe
        if not os.path.exists(imagem_produto):
            mensagem_status.config(text=f"Imagem não encontrada: {imagem_produto}", fg="red")
            return
        
        try:
            # Usando o Pillow para abrir a imagem
            img = Image.open(imagem_produto)
            img = img.resize((200, 200))  # Redimensionando para um tamanho adequado
            img_tk = ImageTk.PhotoImage(img)  # Convertendo para um formato que o Tkinter pode usar
            
            label_imagem.config(image=img_tk)
            label_imagem.image = img_tk  # Mantendo a referência para não perder a imagem
        except Exception as e:
            mensagem_status.config(text=f"Erro ao carregar a imagem: {e}", fg="red")

from tkinter import ttk, messagebox
from PIL import Image, ImageTk

# Dados dos produtos
produtos = {
    'Budweiser 300ml': {'preco': 2.75, 'imagem': 'imagens/budweiser.png'},
    'Corona 330ml': {'preco': 7.50, 'imagem': 'imagens/corona.png'},
    'Amstel Lata 350ml': {'preco': 4.00, 'imagem': 'imagens/amstel_lata.png'},
    'Antarctica 600ml': {'preco': 7.00, 'imagem': 'imagens/antarctica.png'}
}

# Configurações globais
carrinho = {}

# Criando a janela principal
root = tk.Tk()
root.title("Conveniência Online")
root.geometry("1024x600")
root.configure(bg="#FFFFFF")

# Barra superior
top_frame = tk.Frame(root, bg="#FFD700", height=50)
top_frame.pack(fill="x")

titulo = tk.Label(top_frame, text="🍺 Conveniência Online", fg="black", bg="#FFD700", font=("Arial", 16, "bold"))
titulo.pack(side="left", padx=20, pady=5)

# Barra de pesquisa
search_entry = tk.Entry(top_frame, font=("Arial", 12), width=40)
search_entry.pack(side="left", padx=10, pady=5)

search_button = tk.Button(top_frame, text="🔍", font=("Arial", 12), command=lambda: print("Pesquisar"))
search_button.pack(side="left", padx=5)

# Área de produtos com rolagem
canvas_frame = tk.Frame(root)
canvas_frame.pack(fill="both", expand=True)

canvas = tk.Canvas(canvas_frame)
scrollbar = ttk.Scrollbar(canvas_frame, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas)

scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Exibir produtos dinamicamente
row, col = 0, 0
for nome, dados in produtos.items():
    # Carregar imagem
    img = Image.open(dados['imagem']).resize((100, 100))
    img_tk = ImageTk.PhotoImage(img)

    frame_produto = tk.Frame(scrollable_frame, bg="white", bd=2, relief="solid")
    frame_produto.grid(row=row, column=col, padx=10, pady=10)

    label_img = tk.Label(frame_produto, image=img_tk, bg="white")
    label_img.image = img_tk
    label_img.pack()

    label_nome = tk.Label(frame_produto, text=nome, bg="white", font=("Arial", 10, "bold"))
    label_nome.pack()

    label_preco = tk.Label(frame_produto, text=f"R$ {dados['preco']:.2f}", bg="white", fg="green", font=("Arial", 10))
    label_preco.pack()

    btn_adicionar = tk.Button(frame_produto, text="Adicionar", bg="yellow", command=lambda p=nome: print(f"{p} adicionado"))
    btn_adicionar.pack(pady=5)

    col += 1
    if col >= 3:  # Máximo 3 produtos por linha
        col = 0
        row += 1

# Rodar o app
root.mainloop()
