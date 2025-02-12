# Função que verifica se existe dígitos adjacentes iguais
def verifica_digitos_iguais(n):
    # Percorrendo os números lidos
    for i in range(1, len(n)):
        if n[i] == n[i - 1]:
            return "sim"
    return "não"

# Lendo a quantidade de números inteiros
n = int(input("Digite a quantidade de números: "))

# Lendo os números inteiros como uma string contínua
numeros = input(f"Digite {n} números inteiros: ")

# Verificando a condição e exibindo o resultado
resultado = verifica_digitos_iguais(numeros)
print(resultado)