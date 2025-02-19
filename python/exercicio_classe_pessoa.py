class Pessoa:
    def __init__(self, nome='', idade=0, peso=0.0, altura=0.0):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        self.idade += 1
        if self.idade < 21:
            self.altura += 0.5  # Cresce 0,5 cm até os 21 anos

    def engordar(self, peso_ganho):
        self.peso += peso_ganho

    def emagrecer(self, peso_perdido):
        self.peso -= peso_perdido

    def crescer(self, cm_ganho):
        self.altura += cm_ganho

# Testando
pessoa1 = Pessoa('Carlos', 20, 70, 175)
print(pessoa1.nome, pessoa1.idade, pessoa1.peso, pessoa1.altura)

pessoa1.envelhecer()
print(pessoa1.nome, pessoa1.idade, pessoa1.peso, pessoa1.altura)  # A idade e altura mudam

pessoa1.engordar(5)
print(pessoa1.nome, pessoa1.idade, pessoa1.peso, pessoa1.altura)

pessoa1.emagrecer(3)
print(pessoa1.nome, pessoa1.idade, pessoa1.peso, pessoa1.altura)

pessoa1.crescer(2)
print(pessoa1.nome, pessoa1.idade, pessoa1.peso, pessoa1.altura)