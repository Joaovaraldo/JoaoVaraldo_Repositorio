def letra_mais_comum(s):
    
    contagem = {}

    for letra in s:
        if letra.isalpha():  
            letra = letra.lower() 
            if letra in contagem:
                contagem[letra] += 1
            else:
                contagem[letra] = 1

    letra_mais_comum = max(contagem, key=contagem.get)
    
    return letra_mais_comum

s = "Exemplo de string com letras"
resultado = letra_mais_comum(s)
print(f"A letra mais comum é: {resultado}")