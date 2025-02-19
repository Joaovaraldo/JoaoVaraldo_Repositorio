def eh_palindro(texto):
    texto = texto.replace(" ", "")
    if texto == texto[::-1]:
        return "Palíndromo"
    else:
        return "Não é palíndromo"

entrada = input("Digite uma palavra ou frase: ")
print(eh_palindro(entrada))