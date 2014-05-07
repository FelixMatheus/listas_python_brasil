# Problem Set "Class"
# Fonte: http://www.python.org.br/wiki/ListaDeExercicios
# Name: Matheus Felix

# Exercicio 1

#===============================================================================
# Classe Bola: Crie uma classe que modele uma bola:
# 
# Atributos: Cor, circunferência, material
# Métodos: trocaCor e mostraCor
#===============================================================================

class Bola:
        Cor = None
        Circunferencia = None
        Material = None
        
        def __init__(self, cor):
            self.cor = cor
        
        def trocaCor(self, cor):
            self.cor = cor
        
        def mostraCor(self):
            return self.cor

c1 = Bola('amarelo')
c2 = Bola('rosa')
print c1.mostraCor()
print c2.trocaCor()
        
# Exercicio 2

# Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

class Quadrado:
        lado_a = None
        lado_b = None
        def __init__(self, lado_a, lado_b):
            self.lado_a = lado_a
            self.lado_b = lado_b
            print "Criando nova instância do Quadrado"
        def calcula_area(self):
            return self.lado_a * self.lado_b

q1 = Quadrado(1,2)
print q1.calcula_area()

#Auxilio para Implementar!
class No:
    esquerda, direita, valor = None, None, 0
    def __init__(self, valor):
        # construtor dos valores
        self.esquerda = None
        self.direita = None
        self.valor = valor

class Ordenacao:
    def __init__(self):
        # inicializa a raiz da árvore
        self.root = None
    def AdicionaNo(self, valor):
        return No(valor)
    def Inserir(self, raiz, valor):
        # inserir novo valor
        if raiz == None:
            # não há nenhum valor
            return self.AdicionaNo(valor)
        else:
            # já está na árvore
            if valor <= raiz.valor:
                # se os dados forem menores do que os armazenados
                # entra na sub-árvore do lado esquerdo
                raiz.esquerda = self.Inserir (raiz.esquerda, valor)
            else:
            # entra na sub-árvore do lado direito
                raiz.direita = self.Inserir (raiz.direita, valor)
            return raiz

# Exercicio 3

#===============================================================================
# Classe Retangulo: Crie uma classe que modele um retangulo:
# 
# Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
# Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
# Crie um programa que utilize esta classe. 
# Ele deve pedir ao usuário que informe as medidades de um local.
# Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés 
# necessárias para o local.
#===============================================================================

class Retangulo:
        Comprimento = None
        Largura = None
        
        def __init__(self, Comprimento, Largura):
            self.Comprimento = Comprimento
            self.Largura = Largura
            print "Criando nova instância do Retângulo"
            
        def calcula_area(self):
            return self.Comprimento * self.Largura
        
        def calcula_perimetro(self):
            return 2 * self.Comprimento + 2 * self.Largura
        
r1 = Retangulo(3,4)
print r1.calcula_area()