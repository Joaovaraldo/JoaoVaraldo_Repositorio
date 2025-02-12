n = int(input("Digite um numero inteiro positivo :"))
numero = 2
divisores = 0 # divisores variavel contadora

while (numero <= n-1):
    if (n % numero == 0): # se n e divisivel por numero
      divisores = divisores + 1
    numero = numero + 1
if (divisores == 0):
    print("E primo.")
elif (divisores == 0):
    print("Não é primo. Possui 1 divisor diferente de 1 e", n)
else:
    print("Nao e primo. Possui", divisores, "divisores diferentes de 1 e", n)

