# Problem Set "Strings"
# Fonte: http://www.python.org.br/wiki/ListaDeExercicios
# Name: Matheus Felix

# Exercício 1

str1 = raw_input("digite a primeira string: ")
str2 = raw_input("digite a segunda string: ")
numStr1 = len(str1)
numStr2 = len(str2)
 
print "Compara duas strings"
print "Sting 1 : "+str1
print "Sting 2 : "+str2
print "Tamanho de \""+str1+"\" eh: ",numStr1,"caracteres"
print "Tamanho de \""+str2+"\" eh: ",numStr2,"caracteres"
if numStr1 != numStr2:
    print "As duas strings sao de tamanhos diferentes.\n As duas strings possuem conteudo diferente."
elif str1 == str2:
    print "As duas strings sao iguais!"
    
# Exercicio 2

nome = raw_input("digite seu nome: ")
nomeInvert = ""
i = len(nome) - 1
while i >= 0:
    nomeInvert = nomeInvert+nome[i:i+1]
    i = i - 1
print nomeInvert.upper()

# Exercicio 3

nome = raw_input("digite seu nome: ")
i = 0
while i <= len(nome):
    print nome[i:i+1]
    i = i + 1

# Exercicio 4

nome = raw_input("digite seu nome: ")
i = 1
while i < len(nome) + 1:
    print nome[0:i]
    i = i + 1
    
# Exercicio 5

nome = raw_input("digite seu nome ---> ")
i = len(nome)
while i >= 0:
    print nome[0:i]
    i = i - 1

# Exercicio 6

def dataExt(data):
    mesesStr = ["janeiro", "fevereiro", "marco", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
    dia = int(data[0:2])
    mes = int(data[3:5])
    ano = int(data[6:10])
    print "Voce nasceu em",dia,"de",mesesStr[mes-1],"de",ano,"."
 
i = 0
while i == 0:
    dataStr = raw_input("Digite uma data (DD/MM/AAAA): ")
    dataExt(dataStr)
    i = input("\nDigite 0 para continuar ou 1 para sair: ")
    if i == 1:
        print "\nAte a proxima!\n\n"
        
# Exercicio 7