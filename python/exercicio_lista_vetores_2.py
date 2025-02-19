# Lê o número de notas
n = int(input("Digite a quantidade de notas: "))

# Cria uma lista para armazenar as notas
notas = []

# Lê as notas
for i in range(n):
    nota = float(input(f"Digite a nota {i+1}: "))
    notas.append(nota)

# Exibe as notas
for nota in notas:
    print(nota)

# Calcula a média
media = sum(notas) / n

# Exibe a média
print(f"Média: {media}")