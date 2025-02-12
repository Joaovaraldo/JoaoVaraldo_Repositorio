texto = input("Digite um texto: ")
pontuação = [".", ",", ":", ";", "!", "?"]

for p in pontuação:
    texto = texto.replace(p," ")

    numero_palavras = len(texto.split())
    print("Número de palavras:", numero_palavras)