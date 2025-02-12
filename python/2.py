class Pessoa:
    
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome 
        self.idade = idade
        self.peso = peso
        self.altura = altura
    
    def apresentar(self):
        print(f"Nome : {self.nome}")
        print(f"Idade : {self.idade} anos")
        print(f"Peso : {self.peso} kg")
        print(f"Altura : {self.altura} metros")
pessoa1 = Pessoa("Matias ", 12, 80, 1.80)
pessoa1.apresentar()       