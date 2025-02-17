def Lequantidade():
    # Solicita ao usuário que digite um número
    num = input("Digite um numero: ")  
    
    # Calcula a quantidade de caracteres no número digitado
    quantidade_de_numeros = len(num)  
    
    # Retorna a quantidade de caracteres
    return quantidade_de_numeros

# Chama a função e armazena o resultado
resultado = Lequantidade()  

# Exibe a quantidade de dígitos do número digitado
print(resultado)  