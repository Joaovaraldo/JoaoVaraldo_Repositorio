print("Oi, tchau, fica com Deus")
String = input ("Digite uma palabra para saber se ela é um Palíndromo")
inversa = ""

for x in String:
    inversa = x + inversa
print(inversa)

if inversa == String:
   print(" não é um pálindromo! ")
else:
    print(" É um pálindromo! ")