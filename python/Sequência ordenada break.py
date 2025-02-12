n = int(input("Digite uma quantidade de numeros para ser analisada: "))
print("Informe o número: ")
anterior =int(input())

ordenado = True # ordenado é a variavel indicadora

for i in range(n-1):
    print("Informe o número: ")
    atual = int(input())
    if atual < anterior :
        ordenado = False
        break
    anterior = atual

if (ordenado):
    print ("Sequência ordenada.")
else:
    print ("Sequência não ordenada.")