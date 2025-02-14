def leNumeroInt():
    numero = input("Digite um número inteiro: ")
    return int(numero)

def soma(numero1, numero2):
    resultado = numero1 + numero2
    return resultado

n1 = leNumeroInt()
n2 = leNumeroInt()
res = soma(n1, n2)
print("A soma dos numeros é", res)