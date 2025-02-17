def potencia(a, b):
    if b == 0:
        return 1  # Qualquer número elevado a zero é 1
    
    resultado = 1
    
    # Se b é positivo, multiplicamos a por ele mesmo b vezes
    if b > 0:
        for _ in range(b):
            resultado *= a
    
    # Se b é negativo, fazemos 1 / (a^|b|)
    else:
        for _ in range(-b):
            resultado *= a
        resultado = 1 / resultado
    
    return resultado