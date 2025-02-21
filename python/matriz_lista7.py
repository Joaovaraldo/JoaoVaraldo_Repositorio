def somaMatriz(mat1, mat2):
    tam = len(mat1)
    mat3 = [[0 for j in range(tam)] for i in range(tam)]
    for i in range(tam):
        for j in range(tam):
            mat3[i][j] = mat1[i][j] + mat2[i][j]
    return mat3

def imprimeMatriz(mat):
    for linha in mat:
        for numero in linha:
            print(numero, end=" ")
        print()

def leMatriz(dimensao):
    mat = [[] for i in range(dimensao)]
    for i in range(dimensao):
        for j in range(dimensao):
            num = int(input(f"({i+1},{j+1}): "))
            mat[i].append(num)
    return mat

def multiplicaMatriz(mat1, mat2):
    tam = len(mat1)
    mat3 = [[0 for j in range(tam)] for i in range(tam)] 
    
    for i in range(tam):
        for j in range(tam):
            for k in range(tam):
                mat3[i][j] += mat1[i][k] * mat2[k][j] 
    return mat3

n = int(input("Dimensão das matrizes: "))
mat1 = leMatriz(n)
mat2 = leMatriz(n)

print("mat1: ")
imprimeMatriz(mat1)
print("mat2: ")
imprimeMatriz(mat2)

mat3Soma = somaMatriz(mat1, mat2)
print("Soma: ")
imprimeMatriz(mat3Soma)

mat3Mult = multiplicaMatriz(mat1, mat2)
print("Multiplicação: ")
imprimeMatriz(mat3Mult)