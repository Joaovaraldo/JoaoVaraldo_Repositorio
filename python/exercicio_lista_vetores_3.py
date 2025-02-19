# Lê as duas listas
lista1 = [int(x) for x in input("Digite 5 números para a primeira lista separados por espaço: ").split()]
lista2 = [int(x) for x in input("Digite 5 números para a segunda lista separados por espaço: ").split()]

# Encontra os elementos comuns entre as duas listas
comum = [item for item in lista2 if item in lista1]

# Verifica se há elementos em comum e imprime o resultado
if comum:
    for item in comum:
        print(item)
else:
    print("Não tem.")