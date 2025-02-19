# Lê o número n
n = int(input("Digite um número: "))

# Loop para imprimir as linhas
for i in range(1, n + 1):
    # Imprime os números de 1 até i
    print(" ".join(str(x) for x in range(1, i + 1)))