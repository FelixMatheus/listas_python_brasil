#coding: utf-8

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
        
        def __init__(self, cor, Material):
            self.cor = cor
            self.Material = Material
            
        def trocaCor(self, cor):
            self.cor = cor
        
        def mostraCor(self):
            print self.cor

class Teste(object):
    cor = raw_input("Digite uma cor: ")
    Material = raw_input("Digite um material: ")
    bola = Bola(cor, Material)
    bola.mostraCor()
    cor = raw_input("Digite uma cor: ")
    bola.trocaCor(cor)
    bola.mostraCor()
    mat = bola.Material
    print mat

# Exercicio 2

class Quadrado:
    
    def __init__(self, lado):
        self.lado=lado
    def mudarLado(self,lado):
        self.lado=lado
    def retornarLado(self):
        return self.lado
    def calcular_area(self):
        return (self.lado)**2

class Teste1(object):
    lado = int(input("Digite um valor de lado: "))
    quadrado = Quadrado(lado)
    lado = int(input("Digite um valor de lado: "))
    quadrado.mudarLado(lado)
    retorno=quadrado.retornarLado()
    area=quadrado.calcular_area()
    print retorno, area

# Exercicio 3

class Retangulo:
    
    def __init__(self,lado_a,lado_b):
        self.lado_a=lado_a
        self.lado_b=lado_b
    def mudarLado(self, lado_a, lado_b):
        self.lado_a=lado_a
        self.lado_b=lado_b
    def calcula_area(self):
        return (self.lado_a*self.lado_b)
    def calcula_perimetro(self):
        return (2*(self.lado_a))+(2*(self.lado_b))
    
class Teste2(object):
    lado_a=int(input("Digite o lado a: "))
    lado_b=int(input("Digite o lado b: "))
    retangulo = Retangulo(lado_a,lado_b)
    lado_a=int(input("Digite o lado a: "))
    lado_b=int(input("Digite o lado b: "))
    retangulo.mudarLado(lado_a,lado_b)
    area = retangulo.calcula_area()
    perimetro = retangulo.calcula_perimetro()
    print area, perimetro
 
class Teste3(object):
    lado_a=float(input("Medida do Lado A: "))
    lado_b=float(input("Medida do Lado B: "))
    M1=lado_a
    M2=lado_b
    Local = Retangulo(M1,M2)
    lado_a=float(input("Medida do Lado A Piso: "))
    lado_b=float(input("Medida do Lado B Piso: "))
    P1=lado_a
    P2=lado_b
    Piso = Retangulo(P1,P2)
    area1 = Local.calcula_area()
    area2 = Piso.calcula_area()
    Qtd_Piso = area1/area2
    print area1, area2, Qtd_Piso
    lado_a=float(input("Medida Altura Rodape: "))
    lado_b=float(input("Medida Comprimento Rodape: "))
    Alt_R=lado_a
    Comp_R=lado_b
    Rodape = Retangulo(Alt_R, Comp_R)
    NumeroRodapes=(2*(M1/Comp_R))
    NumeroRodapes2=(2*(M2/Comp_R))
    TotalRodapes=(NumeroRodapes+NumeroRodapes2)
    print TotalRodapes

#Exercicio 4

class Pessoa:
    
    def __init__(self, nome, idade, altura, peso):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso
        
    def crescer(self):
        idade = self.idade
        idade2 = (21-idade)
        altura = self.altura
        res = (idade2*0.05)+(altura)
        print res
        return res
    
    def engordar(self):
        return self.peso+5
    def emagrescer(self):
        return self.peso-5
    def envelhecer(self):
        return self.idade
    
class Teste4(object):
     
    nome = raw_input("Digite o Nome: ")
    idade = float(input("Digite a Idade: "))
    altura = float(input("Digite a Altura: "))
    peso = int(input("Digite o Peso: "))
    cresce = Pessoa(nome, idade, altura, peso)
    cresceu = cresce.crescer()
        
#Exercicio 5

class Conta_Corrente:
    
    def __init__(self, n_conta, nome_correntista, saldo=False):
        self.n_conta = n_conta
        self.nome_correntista = nome_correntista
        self.saldo = 0
    
    def alterarNome(self, nome_correntista):
        self.nome_correntista = nome_correntista
      
    def deposito(self):
        return self.n_conta
    
    def saque(self):
        return self.saldo
    
#Exercicio 6

class TV:
    
    def __init__(self, canal, volume, aum, dim):
        self.canal = canal
        self.volume = volume
        self.aum = aum
        self.dim = dim
        
    def verificar_volume(self, volume):
        if (volume>50) or (volume<0):
            print "volume fora da faixa"
        else:
            self.volume = volume
        
    def aumentar_volume(self):
        res = self.volume + self.aum
        if (res<50):
            return res 
        else:
            print "nada"
            
    def diminuir_volume(self):
        res = self.volume - self.dim
        if (res>0):
            return res
        else:
            return "nada"
    
class Teste5(object):    
     
    canal = int(input("Digite o Numero do Canal: "))
    volume = input("Digite o Volume: ")
    aum = input("Digite o Aumento: ")
    dim = int(input("Digite o Diminui: "))
    aumentar = TV(canal, volume, aum, dim)
    aum_vol = aumentar.aumentar_volume()
    diminuir = TV(canal, volume, aum, dim)
    dim_vol = diminuir.diminuir_volume()
    print canal, volume, aum_vol, dim_vol