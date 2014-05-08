# Problem Set "Funções"
# Fonte: http://www.python.org.br/wiki/ListaDeExercicios
# Name: Matheus Felix


#Exercício 1

def imprime(n):
    i = 1
    while i <= n:
        a = i
        b = 0
        while b < i:
            print i, " ",
            b = b + 1
        print "\n"
        i = i + 1
 
numero = input("digite um numero: ")
imprime(numero)

#Exercicio 2

def imprime(n):
    i = 1
    while i <= n:
        a = 1
        b = 0
        while b < i:
            print a, " ",
            a = a + 1
            b = b + 1
        print "\n"
        i = i + 1
 
numero = input("digite um numero:")
imprime(numero)

#Exercicio 3

def soma3(n1, n2, n3):
    return n1 + n2 + n3
 
numeros = [] 
i = 0
while i < 3:
    numero = input("digite um numero: ")
    numeros.append(numero)
    i = i + 1
 
print "soma dos 3 numeros digitados: ", soma3(numeros[0], numeros[1], numeros[2])

#Exercicio 4

def pOrN(n):
    if n > 0:
        print "P"
    else:
        print "N"
 
numero = input("digite um numero: ")
pOrN(numero)

#Exercicio 5

def somaImposto(taxaImposto, custo):
    return custo + custo*(float(taxaImposto)/100)
 
custo = input("digite o custo do produto: ")
taxaImposto = input("digite a taxa (%) de imposto: ")
 
print "R$ ",somaImposto(taxaImposto, custo)

def converteHora(hh, mm):
    if hh > 12:
        return hh - 12
    elif hh == 0:
        return 12
    else:
        return hh
 
def printHora(hh, mm):
    if hh >= 12:
        print str(converteHora(hh,mm))+":"+str(mm)+" PM"
    elif hh == 0:
        print "12:"+str(mm)+" AM"
    else:
        print str(hh)+":"+str(mm)+" AM"
 
i = 0
while i != 1:
    print "\nConversor de hora\n"
    hora = raw_input("digite a hora que deseja converter de 24 para 12h (hh:mm): ")
    hh = int(hora[0:2])
    mm = hora[3:5]
    print "\n"
    printHora(hh,mm)
    i = input("\nDigite 0 para conitnuar ou 1 para sair ---> ")
    while i != 0 and i != 1:
            i = input("\nDigite 0 para conitnuar ou 1 para sair ---> ")
    if i == 1:
        print "\n Ate a proxima!!"
        
#Exercicio 7

def valorPagamento(valorPrest, diasAtr):
    pgt = valorPrest
    prestJuros = valorPrest
    multa = valorPrest*0.03
    if diasAtr > 0:
        i = 0
        while i < diasAtr:
            prestJuros = prestJuros + prestJuros*0.001
            i = i + 1
        juros = prestJuros - valorPrest
        return float(multa + valorPrest + juros)
    else:
        return float(valorPrest)
 
i = 0
while i == 0:
    valorPrest = input("Digite o valor da prestacao: ")
    diasAtr = input("Digite o numero de dias de atraso: ")
    print "total a pagar: R$", valorPagamento(valorPrest, diasAtr)
    i = input("\nDigite 0 para continuar ou 1 para sair: ")
    if i == 1:
        print "\nAte a proxima!\n\n"
        
#Exercicio 8

def qtyDigitos(numero):
    numeroStr = str(numero)
    return len(numeroStr)
 
i = 0
while i == 0:
    numero = input("Digite um numero: ")
    print "qty de algarismos do numero digitado: ", qtyDigitos(numero)
    i = input("\nDigite 0 para continuar ou 1 para sair: ")
    if i == 1:
        print "\nAte a proxima!\n\n"
        
#Exercicio 9

def reversoNumero(numero):
    numeroStr = str(numero)
    i = len(numeroStr)
    numeroInvertStr = ""
    while i > 0:
        numeroInvertStr = numeroInvertStr+numeroStr[i-1:i]
        i = i - 1
    numeroInvert = int(numeroInvertStr)
    return numeroInvert
 
i = 0
while i == 0:
    numero = input("digite um numero: ")
    print "o numero digitado invertido eh igual: ", reversoNumero(numero)
    i = input("\nDigite 0 para continuar ou 1 para sair: ")
    if i == 1:
        print "\nAte a proxima!\n\n"
        
#Exercicio 11

def dataExt(data):
    mesesStr = ["janeiro", "fevereiro", "marco", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
    dia = int(data[0:2])
    mes = int(data[3:5])
    ano = int(data[6:10])
    print dia,"de",mesesStr[mes-1],"de",ano
 
i = 0
while i == 0:
    dataStr = raw_input("Digite uma data (DD/MM/AAAA): ")
    dataExt(dataStr)
    i = input("\nDigite 0 para continuar ou 1 para sair: ")
    if i == 1:
        print "\nAte a proxima!\n\n"
        
#Exercicio 12

import random
 
def embaralha(palavra):
    n = len(palavra)
    i = 0
    letras = []
    while i < len(palavra):
        letras.append(palavra[i:i+1])
        i = i + 1
 
    indiceSort = range(len(letras))
 
    resultList = []
    i = 0
    while len(indiceSort) > 0:
        indice = random.choice(indiceSort)
        resultList.append(letras[indice])
        indiceSort.remove(indice)
        i = i + 1
 
    resultStr = ""
    i = 0
    while i < len(resultList):
        resultStr = resultStr+resultList[i]
        i = i + 1
    print resultStr
 
i = 0
while i == 0:
    palavraEntrada = raw_input("digite um palavra que sera embaralhada---> ")
    print "palavra nova ---> ", embaralha(palavraEntrada)
    i = input("\nDigite 0 para continuar ou 1 para sair ---> ")
    if i == 1:
        print "\nAte a proxima!\n\n"


        