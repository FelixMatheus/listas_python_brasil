# "Estrutura Sequencial"
# Fonte: http://www.python.org.br/wiki/ListaDeExercicios
# Name: Matheus Felix

# Exercicio 1

print("Ola Mundo!")

# Exercicio 2

number = input("Digite um numero: ")
print "O numero digitado foi ", number

# Exercicio 3

number1 = input("Digite um numero: ")
number2 = input("Digite outro numero: ")
print "Soma dos numeros digitados = ", number1 + number2

# Exercicio 4

nota1 = input("digite sua primeira nota bimestral: ")
nota2 = input("digite sua segunda nota bimestral: ")
nota3 = input("digite sua terceira nota bimestral: ")
nota4 = input("digite sua quarta nota bimestral: ")
print " sua media é: ", (nota1+nota2+nota3+nota4)/4

# Exercicio 5

print "Conversor de metro para centimetro"
number1 = input("digite o valor em metros que deseja converter para centimetros: ")
 
print " esse valor equivale: ", number1*100, " cm"


# Exercicio 6

raio = input("digite o raio do circulo: ")
area = 3.14*raio*raio
print "area do circulo: ", area

# Exercicio 7

import math
 
lado = input("o lado do quadrado: ")
area = math.pow(lado,2)
print "area do quadrado eh: ", area
print "o dobro da area eh: ", area*2

# Exercicio 8

import math

horaTrabalho = input("quanto voce ganha por hora? ")
horaTrabalhada = input("quantas horas voce trabalho no mes? ")
print "Voce Ganhou R$ ", horaTrabalho*horaTrabalhada

# Exercicio 9

f = input("digite o valor de graus farenheit: ")
c = (5.0*(f-32.0)/9.0)
print c," celcius"

# Exercicio 10

c = input("digite o valor de graus celsius: ")
f = 32.0 + (9.0*c)/5
print f," farenheit"

# Exercicio 11

import math
 
a = input("digite um numero inteiro: ")
b = input("digite um numero real: ")
c = input("digite um numero real: ")
 
print "-> ", a*b
print "--> ", a*3 + c
print "---> ", math.pow(c,3)

# Exercicio 12

 
altura = input("digite sua altura em metros: ")
pesoIdeal = (72.7*altura)-58
print "peso ideal: ", pesoIdeal, " kg"

# Exercicio 13

print "calculo de peso ideal"
print "-------------------------"
sexo = input("Digite seu sexo \"M\" ou \"F\" ---> ")
altura = input("digite sua altura em metros ---> ")
if sexo == "M" or sexo == "m":
    pesoIdeal = (72.7*altura)-58
    print "peso ideal: ", pesoIdeal, " kg" 
else:
    pesoIdeal = (62.1*altura)-44.7
    print "peso ideal: ", pesoIdeal, " kg"
    
# Exercicio 14
 
peso = input("quantos quilos de peixe foram pescados? ")
pesoExcedente = 0.0
multa = 0.0
multaPorPesoExcedente = 4.00
if peso > 50.0:
    pesoExcedente = peso - 50.0
    multa = pesoExcedente*multaPorPesoExcedente
    print "peso excedente: ", pesoExcedente
    print "multa de R$ ", multa
else:
    print "peso excedente: ", pesoExcedente
    print "multa de R$ ", multa
    
# Exercicio 15

iR = 0.11
iNss = 0.08
taxaSindicato = 0.05
horaTrabalho = input("quanto voce ganha por hora? ")
horaTrabalhada = input("quantas horas voce trabalho no mes? ")
salarioBruto = float(horaTrabalho*horaTrabalhada)
pagamentoDeIr = salarioBruto*iR
pagamentoDeInss = salarioBruto*iNss
pagamentoDeSindicato = salarioBruto*taxaSindicato
salarioLiquido = salarioBruto - pagamentoDeIr - pagamentoDeInss - pagamentoDeSindicato
 
print "salario Bruto R$ ", salarioBruto
print "desconto de IR R$ ", pagamentoDeIr
print "desconto de INSS R$ ", pagamentoDeInss
print "desconto de taxa de Sindicato R$ ", pagamentoDeSindicato
print "salario liquido R$ ", salarioLiquido

# Exercicio 16

area = input("quantos metros quadrados serao pintados? ")
qtyLitros = area/3
precoLata = 80.0
capacidadeLata = 18
qtyLatas = qtyLitros/capacidadeLata
valorTotal = qtyLatas*precoLata
print "qty latas: ", qtyLatas
print "valor R$ ", valorTotal

# Exercicio 17

area = input("quantos metros quadrados serao pintados? ")
qtyLitros = area/3
capacidadeLata = 18.0
precoLata = 80.0
capacidadeGalao = 3.6
precoGalao = 25.0
qtyLatas = qtyLitros/capacidadeLata
valorTotalLata = qtyLatas*precoLata
qtyGalao = qtyLitros/capacidadeGalao
valorTotalGalao = qtyLatas*precoGalao
 
print "qty latas ", qtyLatas
print "valor latas R$ ", valorTotalLata
print "qty galao ", qtyGalao
print "valor galao R$ ", valorTotalGalao

