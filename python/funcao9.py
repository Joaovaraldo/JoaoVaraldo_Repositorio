def leNumero(numero):
    if numero > 0:
        return 'P'

    if numero < 0:
        return 'N'

    else:
        return 'Z'

numero = float(input("Digite um numero: "))
resultado = leNumero(numero)
print(f'O resultado é: {resultado}')    