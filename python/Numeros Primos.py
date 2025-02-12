n = int(input("Digite um numero inteiro positivo: "))
numero = 2 
primo = True # Primo é a variavel indicadora

while (numero <= n-1) and (primo):
    if (n % numero == 0): # Se n é divisel por numero
        primo = False
    numero = numero + 1
if (primo):
    print("É primo.")
else:
    print("Não é primo.")