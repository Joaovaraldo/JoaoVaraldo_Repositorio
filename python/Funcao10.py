def inverte(numeros):
    # Converte o número para string e inverte usando slicing
    return str(numeros)[::-1]

# Solicita ao usuário que digite um número
numeros = input("Digite um numero: ")

# Chama a função inverte passando o número digitado e armazena o resultado
resultado = inverte(numeros)

# Exibe o número invertido
print(resultado)