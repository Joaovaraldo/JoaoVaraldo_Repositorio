def leNota(num):
    notas = []
    for i in range(num):
        dado = float(input("Digite sua nota: "))
        notas.append(dado)
    return notas

def calculaMedia(notas):
    soma = 0
    for i in range(len(notas)):
        soma = soma + notas[i]
    return(soma/len(notas))

    n = int(input("Digite o número de notas: "))
notas = leNota(n)
print("As notas são:", notas)
media = calculaMedia(notas)
print("A media é:", format(media, ".1f"))