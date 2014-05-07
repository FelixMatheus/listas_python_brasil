# "Estrutura de Decisão"
# Fonte: http://www.python.org.br/wiki/ListaDeExercicios
# Name: Matheus Felix

#Exercicio 1

number1 = input("digite um numero: ")
number2 = input("digite outro numero: ")
if number1 > number2:
    print "o maior numero eh: ", number1
if number2 > number1:
    print "o maior numero eh: ", number2
else:
    print number1, " = ", number2
    
#Exercicio 2

number1 = input("digite um numero: ")
if number1 > 0:
    print number1, " eh positivo "
if number1 < 0:
    print number1, " eh negativo "
else:
    print number1, " eh ZERO "
    
#Exercicio 3

sexo = input("digite seu sexo \"F\" ou \"M\": ")
if sexo == "F" or sexo == "M":
    if sexo == "F":
        print "F - Feminino"
    else:
        print "M - Masculino"
else:
    print "sexo invalido"
    
#Exercicio 4
 
letra = raw_input("digite uma letra (ex: \"a\") : ")
if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    print letra, "eh uma vogal"
else:
    print letra, "eh uma consoante"
        
#Exercicio 5
 
nota1 = input("digite sua primeira nota: ")
nota2 = input("digite sua segunda nota: ")
media = (float(nota1)+float(nota2))/2
if media >= 7.0:
    if media == 10.0:
        print "Aprovado con distincao!"
    else:
        print "Aprovado"
else:
    print "Reprovado"

#Exercicio 6
 
number1 = input("digite um numero: ")
number2 = input("digite um numero: ")
number3 = input("digite um numero: ")
if (number1 > number2) and (number1 > number3):
    print number1, "eh o maior numero" 
if (number2 > number1) and (number2 > number3):
    print number2, "eh o maior numero"
if (number3 >number1) and (number3 > number2):
    print number3, "eh o maior numero"
    
#Exercicio 7

number1 = input("digite um numero: ")
number2 = input("digite um numero: ")
number3 = input("digite um numero: ")
if (number1 > number2) and (number1 > number3):
    print number1, "eh o maior numero" 
if (number2 > number1) and (number2 > number3):
    print number2, "eh o maior numero"
if (number3 >number1) and (number3 > number2):
    print number3, "eh o maior numero" 
if (number1 < number2) and (number1 < number3):
    print number1, "eh o menor numero" 
if (number2 < number1) and (number2 < number3):
    print number2, "eh o menor numero"
if (number3 <number1) and (number3 < number2):
    print number3, "eh o menor numero"

#Exercicio 8

produto1 = input("digite o preco do produto 1: ")
produto2 = input("digite o preco do produto 2: ")
produto3 = input("digite o preco do produto 3: ")
 
if (produto1 < produto2) and (produto1 < produto3):
    print "compre produto 1" 
if (produto2 < produto1) and (produto2 < produto3):
    print "compre produto 2" 
if (produto3 <produto1) and (produto3 < produto2):
    print "compre produto 3"
    
#Exercicio 9
 
number1 = input("digite um numero: ")
number2 = input("digite um numero: ")
number3 = input("digite um numero: ")
if (number1 > number2) and (number1 > number3) and (number2 > number3):
    print number1 , " ", number2, " ", number3
if (number1 > number2) and (number1 > number3) and (number3 > number2):
    print number1 , " ", number3, " ", number2
if (number2 > number1) and (number2 > number3) and (number1 > number3):
    print number2 , " ", number1, " ", number3
if (number2 > number1) and (number2 > number3) and (number3 > number1):
    print number2 , " ", number3, " ", number1
if (number3 > number1) and (number3 > number2) and (number1 > number2):
    print number3 , " ", number1, " ", number2
if (number3 > number1) and (number3 > number2) and (number2 > number1):
    print number3 , " ", number2, " ", number1

#Exercicio 10

turno = raw_input("digite seu turno M-matutino ou V-Vespertino ou N- Noturno ---> ")
if turno == "M" or turno == "m":
    print("bom dia")
if turno == "V" or turno == "v":
    print("boa tarde")
if turno == "N" or turno == "n":
    print("boa noite")

#Exercicio 11

salarioAjustado = 0
aumentoPer = 0
aumentoVal = 0
salario = float(raw_input("digite seu salario: "))
if salario <= 280:
    aumentoPer = 0.2
    aumentoVal = aumentoPer*salario
    salarioAjustado = salario*(1 + aumentoPer)
if 280 < salario <= 700:
    aumentoPer = 0.15
    aumentoVal = aumentoPer*salario
    salarioAjustado = salario*(1 + aumentoPer)
if 700 < salario <= 1500:
    aumentoPer = 0.1
    aumentoVal = aumentoPer*salario
    salarioAjustado = salario*(1 + aumentoPer)
if 1500 < salario:
    aumentoPer = 0.05
    aumentoVal = aumentoPer*salario
    salarioAjustado = salario*(1 + aumentoPer)
print "salario - R$ ", salario
print "percentual de aumnento aplicado - ", aumentoPer*100, "%"
print "valor do aumento - R$ ", aumentoVal
print "salario ajustado - R$ ", salarioAjustado

#Exercicio 12

taxaIrList = [0.0, 0.05, 0.1, 0.2]
horasTrabalho = float(raw_input("digite a quantidade de horas trabalhadas: "))
valorHora = float(raw_input("digite o valor em reais da sua hora de trabalho: "))
salarioBruto = horasTrabalho*valorHora
taxaInss = 0.1
fgts = 0.11
if salarioBruto <= 900:
    taxaIr = taxaIrList[0]
if 900 < salarioBruto <= 1500:
    taxaIr = taxaIrList[1]
if 1500 < salarioBruto <= 2500:
    taxaIr = taxaIrList[2]
if salarioBruto > 2500:
    taxaIr = taxaIrList[3]
descontos = (salarioBruto*taxaIr) + (salarioBruto*taxaInss)
print "Salario Bruto: (", valorHora, " * ", horasTrabalho, ") ----> R$ ", salarioBruto
print "(-) IR (", taxaIr*100,"%) ----> R$ ", salarioBruto*taxaIr
print "(-) INSS (", taxaInss*100,"%) ----> R$ ", salarioBruto*taxaInss
print "FGTS (11%) ----> R$ ", salarioBruto*fgts
print "Salario Liquido R$ ----> ", salarioBruto - descontos

#Exercicio 13

dia = input("digite um numero de 1 a 7 referente ao dia da semana ---> ")
if dia == 1 or dia == 2 or dia == 3 or dia == 4 or dia == 5 or dia == 6 or dia == 7:
    if dia == 1:
        print("domingo")
    if dia == 2:
        print("segunda")
    if dia == 3:
        print("terca")
    if dia == 4:
        print("quarta")
    if dia == 5:
        print("quinta")
    if dia == 6:
        print("sexta")
    if dia == 7:
        print("sabado")
else:
    print("numero invalido!!!")
    
#Exercicio 14

nota1 = input("digite sua primeira nota ---> ")
nota2 = input("digite sua segunda nota ---> ")
media = (float(nota1)+float(nota2))/2
 
if 9.0<= media:
    conceito = "A"
if 7.5 <= media < 9.0:
    conceito = "B"
if 6.0 <= media < 7.5:
    conceito = "C"
if 4.0 <= media < 6.0:
    conceito = "D"
if 0.0 <= media < 4.0:
    conceito = "E"
 
if conceito == "A" or conceito == "B" or conceito == "C":
    situacao = "Aprovado"
else:
    situacao = "Reprovado"
 
print "media - ", media
print "conceito - ", conceito
print "situacao - ", situacao

#Exercicio 15

lado1 = float(input("digite o primeiro lado ---> "))
lado2 = float(input("digite o segundo lado ---> "))
lado3 = float(input("digite o terceiro lado ---> "))
 
if (lado1 + lado2) > lado3 and (lado1 + lado3) > lado2 and (lado2 + lado3) > lado1:
    if lado1 == lado2 == lado3:
        print("triangulo equilatero")
    if (lado1 == lado2 and lado3 != lado1) or (lado1 == lado3 and lado2 != lado1) or (lado2 == lado3 and lado2 != lado1):
        print("triangulo isosceles")
    if lado1 != lado2 != lado3:
        print("triango escaleno")
else:
    print("os lados nao formam um triangulo")
    
#Exercicio 16

import math
 
print("digite os termos da equacao a, b e c da equacao ax^2 + bx + c")
a = input("digite o termo a ---> ")
if a == 0:
    print("nao eh uma equacao de segundo grau")
else:
    b = input("digite o termo b  ---> ")
    c = input("digite o termo c ---> ")
    delta = (math.pow(b,2) - (4*a*c))
    if delta < 0:
        print "delta = ",delta," a equacao nao possui raizes reais"
    if delta == 0:
        print "delta = ",delta," a equacao possui uma raiz"
        raiz = ((-1)*b + math.sqrt(delta))/(2*a)
        print "raiz da equacao = ", raiz
    if delta > 0:
        print "delta = ",delta," a equacao possui duas raizes"
        raiz1 = ((-1)*b + math.sqrt(delta))/(2*a)
        raiz2 = ((-1)*b - math.sqrt(delta))/(2*a)
        print "raiz1 da equacao = ", raiz1
        print "raiz2 da equacao = ", raiz2
 


#Exercicio 17
 
ano = input("digite um ano (XXXX): ")
if (ano%4 == 0 and ano%100!= 0) or ano%400 == 0:
    print ano, " eh bissexto"
else:
    print ano, " nao eh bissexto"
    

#Exercicio 18

data = raw_input("digite uma data com o seguinte formato dd/mm/aaaa: ")
dia = int(data[0:2])
mes = int(data[3:5])
ano = int(data[6:10]) 
validade = "true"
i = 0

while validade == "true" and i == 0:
    if (ano%4 == 0 and ano%100!= 0) or ano%400 == 0:
        bissexto = "sim"
    else:
        bissexto = "nao"
    if mes < 1 or mes > 12:
        validade = "false"
    if dia > 31 or ((mes == 4 or mes == 6 or mes == 9 or mes == 11) and dia > 30):
        validade = "false"
    if (mes == 2 and bissexto == "nao" and dia > 28) or ( mes == 2 and bissexto == "sim" and dia > 29):
        validade = "false"
    i = i + 1
 
if validade == "true":
    print("data valida")
else:
    print("data invalida")
    
#Exercicio 19
 
numero = input("digite um numero menor que 1000 ---> ")
numeroStr = str(numero)
qtNumero = len(numeroStr)
 
if qtNumero == 3:
    centena = numeroStr[0:1]
    dezena = numeroStr[1:2]
    unidade = numeroStr[2:3]
    print numeroStr+" = "+centena+" centenas , "+dezena+" dezenas, "+unidade+ " unidades"
 
if qtNumero == 2:
    dezena = numeroStr[0:1]
    unidade = numeroStr[1:2]
    print numeroStr+" = "+dezena+" dezenas, "+unidade+ " unidades"
 
if qtNumero == 1:
    unidade = numeroStr[0:1]
    print numeroStr+" = "+unidade+ " unidades"
    
#Exercicio 21
 
numero = input("digite o valor a ser sacado (entre 10 e 600 reais) ---> ")
numeroStr = str(numero)
qtNumero = len(numeroStr)
nota100 = "nota(s) de cem"
nota50 = "nota(s) de cinquenta"
nota10 = "nota(s) de dez"
nota5 = "nota(s) de cinco"
nota1 = "nota(s) de um"
 
if qtNumero == 3:
    centena = int(numeroStr[0:1])
    dezena = int(numeroStr[1:2])
    unidade = int(numeroStr[2:3])
    print centena, nota100
    if 0 < dezena < 5:
        print dezena, nota10
    if dezena == 5:
        print "1", nota50
    if dezena > 5:
        print "1", nota50
        print (dezena - 5), nota10
    if 0 < unidade < 5:
        print unidade, nota1
    if unidade == 5:
        print unidade, nota5
    if unidade > 5:
        print "1", nota5
        print (unidade - 5), nota1
 
if qtNumero == 2:
    dezena = int(numeroStr[0:1])
    unidade = int(numeroStr[1:2])
    if 0 < dezena < 5:
        print dezena, nota10
    if dezena == 5:
        print "1", nota50
    if dezena > 5:
        print "1", nota50
        print (dezena - 5), nota10
    if 0 < unidade < 5:
        print unidade, nota1
    if unidade == 5:
        print unidade, nota5
    if unidade > 5:
        print "1", nota5
        print (unidade - 5), nota1
 
if qtNumero == 1:
    unidade = int(numeroStr[0:1])
    if 0 < dezena < 5:
        print dezena, nota10
    if 0 < unidade < 5:
        print unidade, nota1
    if unidade == 5:
        print unidade, nota5
    if unidade > 5:
        print "1", nota5
        print (unidade - 5), nota1

#Exercicio 22

numero = input("digite um numero ---> ")
resto = numero%2
if resto == 0:
    print numero, "eh par!"
else:
    print numero, "eh impar!"
    
#Exercicio 23

numero = input("digite um numero ---> ")
 
if round(numero) == numero:
    print numero, " ---> numero inteiro!"
else:
    print numero, " ---> numero decimal"

#Exercicio 24

operacao = raw_input("qual operacao deseja efetuar? digite ADICAO, SUBTRACAO, MULTIPLICACAO, DIVISAO ---> ")
numero1 = input("digite um numero ---> ")
numero2 = input("digite outro numero ---> ")
 
if operacao == "ADICAO" or operacao == "adicao":
    resultado = numero1 + numero2
    print numero1, " + ", numero2, " = ", resultado    
    if resultado%2 == 0:
        print resultado, "eh par"
    else:
        print resultado, "eh impar"
    if resultado >= 0:
        print resultado, "eh positivo"
    else:
        print resultado, "eh negativo"
    if round(resultado) == resultado:
        print resultado, "eh inteiro"
    else:
        print resultado, "eh decimal"
 
if operacao == "SUBTRACAO" or operacao == "subtracao":
    resultado = numero1 - numero2
    print numero1, " - ", numero2, " = ", resultado    
    if resultado%2 == 0:
        print resultado, "eh par"
    else:
        print resultado, "eh impar"
    if resultado >= 0:
        print resultado, "eh positivo"
    else:
        print resultado, "eh negativo"
    if round(resultado) == resultado:
        print resultado, "eh inteiro"
    else:
        print resultado, "eh decimal"
 
if operacao == "MULTIPLICACAO" or operacao == "multiplicacao":
    resultado = numero1 * numero2
    print numero1, " X ", numero2, " = ", resultado    
    if resultado%2 == 0:
        print resultado, "eh par"
    else:
        print resultado, "eh impar"
    if resultado >= 0:
        print resultado, "eh positivo"
    else:
        print resultado, "eh negativo"
    if round(resultado) == resultado:
        print resultado, "eh inteiro"
    else:
        print resultado, "eh decimal"
 
if operacao == "DIVISAO" or operacao == "divisao":
    resultado = numero1 / numero2
    print numero1, " / ", numero2, " = ", resultado    
    if resultado%2 == 0:
        print resultado, "eh par"
    else:
        print resultado, "eh impar"
    if resultado >= 0:
        print resultado, "eh positivo"
    else:
        print resultado, "eh negativo"
    if round(resultado) == resultado:
        print resultado, "eh inteiro"
    else:
        print resultado, "eh decimal"
        
#Exercicio 25
 
print "RESPONDA SIM OU NAO"
 
resp1 = raw_input("telefonou para a vitima? ")
if resp1 == "sim" or resp1 == "SIM":
    peso1 = 1
else:
    peso1 = 0
 
resp2 = raw_input("esteve no local do crime? ")
if resp2 == "sim" or resp2 =="SIM":
    peso2 = 1
else:
    peso2 = 0
 
resp3 = raw_input("mora perto da vitima? ")
if resp3 == "sim" or resp3 =="SIM":
    peso3 = 1
else:
    peso3 = 0
 
resp4 = raw_input("devia para a vitima? ")
if resp4 == "sim" or resp4 =="SIM":
    peso4 = 1
else:
    peso4 = 0
 
resp5 = raw_input("ja trabalhou com a vitima? ")
if resp5 == "sim" or resp5 =="SIM":
    peso5 = 1
else:
    peso5 = 0
 
pesoTotal = peso1 + peso2 + peso3 + peso4 + peso5
 
if pesoTotal == 5:
    print "\nvoce eh o assasino"
if 3 <= pesoTotal < 5:
    print "\nvoce eh cumplice"
if pesoTotal == 2:
    print "\nvoce eh suspeito"
    
#Exercicio 26
 
#valores fixos
precoA = 1.9
precoG = 2.5
descA1 = 0.03
descA2 = 0.05
descG1 = 0.04
descG2 = 0.06
 
tipoComb = raw_input("digite qual o combustivel : A - Alcool ou G - Gasolina ---> ")
litros = input("Quantos litros serao comprados ---> ")
 
if tipoComb == "A" or tipoComb == "a":
    combustivel = "Alcool"
    if litros <= 20:
        totalApagar = litros*precoA*(1 - descA1)
    if litros > 20:
        totalApagar = litros*precoA*(1 - descA2)
 
if tipoComb == "G" or tipoComb == "g":
    combustivel = "Gasolina"
    if litros <= 20:
        totalApagar = litros*precoG*(1 - descG1)
    if litros > 20:
        totalApagar = litros*precoG*(1 - descG2)
 
print "voce ira abastecer seu automovel com "+combustivel
print "Pagara R$ ", totalApagar, "por ",litros, "litros de "+combustivel

#Exercicio 27
 
#valores fixos
precoMorango1 = 2.5
precoMorango2 = 2.2
precoMaca1 = 1.8
precoMaca2 = 1.5
 
qtyMorango = input("quantos kg de morango ---> ")
qtyMaca = input("quantos kg de maca ---> ")
 
if qtyMorango <= 5:
    totalApagarMorango = qtyMorango*precoMorango1
if qtyMorango > 5:
    totalApagarMorango = qtyMorango*precoMorango2
 
if qtyMaca <= 5:
    totalApagarMaca = qtyMaca*precoMaca1
if qtyMaca > 5:
    totalApagarMaca = qtyMaca*precoMaca2
 
totalApagar = totalApagarMorango + totalApagarMaca
 
if (qtyMorango + qtyMaca) > 8 or totalApagar > 25:
    totalApagar = totalApagar - totalApagar*0.1
 
print "total a pagar R$ ", totalApagar

#Exercicio 28
 
#valores fixos
precoFileDuplo1 = 4.9
precoFileDuplo2 = 5.8
precoAlcatra1 = 5.9
precoAlcatra2 = 6.8
precoPicanha1 = 6.9
precoPicanha2 = 7.8
descCartao = 0.05
 
print "Temos File Duplo, Alcatra e  Picanha. Voce pode escolher ate 2 tipos de carne!"
qtyTipos = input("quantos tipos de carne voce quer 1 ou 2 ? ---> ")
 
if qtyTipos == 1:
    tipo1 = raw_input("Escolha: F - File Duplo, A - Alcatra, P - Picanha ---> ")
    qty1 = input("quantos quilos de carne? ---> ")
    tipoPagamento = raw_input("pagamento com cartao tabajara? S - sim ou N - nao ---> ")
 
    if tipo1 == "F" or tipo1 == "f":
        if qty1 <= 5 and (tipoPagamento == "N" or tipoPagamento == "n"):
            totalApagar = precoFileDuplo1*qty1
            print "\npreco por KG eh de R$", precoFileDuplo1
            print "total a pagar eh de R%", totalApagar
        if qty1 <= 5 and (tipoPagamento == "S" or tipoPagamento == "s"):
            totalApagar = precoFileDuplo1*qty1
            valorDescCart = totalApagar*descCartao
            print "\npreco por KG eh de R$ ", precoFileDuplo1
            print "total a pagar eh de R$ ", totalApagar
            print "valor desc Cartao Tabajara R$ ", valorDescCart
            print "total a pagar com desconto R% ", totalApagar - valorDescCart
 
        if qty1 > 5 and (tipoPagamento == "N" or tipoPagamento == "n"):
            totalApagar = precoFileDuplo2*qty1
            print "\npreco por KG eh de R$", precoFileDuplo2
            print "total a pagar eh de R%", totalApagar
        if qty1 > 5 and (tipoPagamento == "S" or tipoPagamento == "s"):
            totalApagar = precoFileDuplo2*qty1
            valorDescCart = totalApagar*descCartao
            print "\npreco por KG eh de R$ ", precoFileDuplo2
            print "total a pagar eh de R$ ", totalApagar
            print "valor desc Cartao Tabajara R$ ", valorDescCart
            print "total a pagar com desconto R% ", totalApagar - valorDescCart
 
    if tipo1 == "A" or tipo1 == "a":
        if qty1 <= 5 and (tipoPagamento == "N" or tipoPagamento == "n"):
            totalApagar = precoAlcatra1*qty1
            print "\npreco por KG eh de R$", precoAlcatra1
            print "total a pagar eh de R%", totalApagar
        if qty1 <= 5 and (tipoPagamento == "S" or tipoPagamento == "s"):
            totalApagar = precoAlcatra1*qty1
            valorDescCart = totalApagar*descCartao
            print "\npreco por KG eh de R$ ", precoAlcatra1
            print "total a pagar eh de R$ ", totalApagar
            print "valor desc Cartao Tabajara R$ ", valorDescCart
            print "total a pagar com desconto R% ", totalApagar - valorDescCart
 
        if qty1 > 5 and (tipoPagamento == "N" or tipoPagamento == "n"):
            totalApagar = precoAlcatra2*qty1
            print "\npreco por KG eh de R$", precoAlcatra2
            print "total a pagar eh de R%", totalApagar
        if qty1 > 5 and (tipoPagamento == "S" or tipoPagamento == "s"):
            totalApagar = precoAlcatra2*qty1
            valorDescCart = totalApagar*descCartao
            print "\npreco por KG eh de R$ ", precoAlcatra2
            print "total a pagar eh de R$ ", totalApagar
            print "valor desc Cartao Tabajara R$ ", valorDescCart
            print "total a pagar com desconto R% ", totalApagar - valorDescCart
 
    if tipo1 == "P" or tipo1 == "p":
        if qty1 <= 5 and (tipoPagamento == "N" or tipoPagamento == "n"):
            totalApagar = precoPicanha1*qty1
            print "\npreco por KG eh de R$", precoPicanha1
            print "total a pagar eh de R%", totalApagar
        if qty1 <= 5 and (tipoPagamento == "S" or tipoPagamento == "s"):
            totalApagar = precoPicanha1*qty1
            valorDescCart = totalApagar*descCartao
            print "\npreco por KG eh de R$ ", precoPicanha1
            print "total a pagar eh de R$ ", totalApagar
            print "valor desc Cartao Tabajara R$ ", valorDescCart
            print "total a pagar com desconto R% ", totalApagar - valorDescCart
 
        if qty1 > 5 and (tipoPagamento == "N" or tipoPagamento == "n"):
            totalApagar = precoPicanha2*qty1
            print "\npreco por KG eh de R$", precoPicanha2
            print "total a pagar eh de R%", totalApagar
        if qty1 > 5 and (tipoPagamento == "S" or tipoPagamento == "s"):
            totalApagar = precoPicanha2*qty1
            valorDescCart = totalApagar*descCartao
            print "\npreco por KG eh de R$ ", precoPicanha2
            print "total a pagar eh de R$ ", totalApagar
            print "valor desc Cartao Tabajara R$ ", valorDescCart
            print "total a pagar com desconto R% ", totalApagar - valorDescCart
 
if qtyTipos == 2:
    tipo1 = raw_input("Escolha: F - File Duplo, A - Alcatra, P - Picanha ---> ")
    qty1 = input("quantos quilos de carne? ---> ")
    tipo2 = raw_input("Escolha: F - File Duplo, A - Alcatra, P - Picanha ---> ")
    qty2 = input("quantos quilos de carne? ---> ")
    tipoPagamento = raw_input("pagamento com cartao tabajara? S - sim ou N - nao ---> ")
 
    if tipo1 == "F" or tipo1 == "f":
        if qty1 <= 5 and (tipoPagamento == "N" or tipoPagamento == "n"):
            totalApagar = precoFileDuplo1*qty1
            print "\npreco por KG eh de R$", precoFileDuplo1
            print "total a pagar eh de R%", totalApagar
        if qty1 <= 5 and (tipoPagamento == "S" or tipoPagamento == "s"):
            totalApagar = precoFileDuplo1*qty1
            valorDescCart = totalApagar*descCartao
            print "\npreco por KG eh de R$ ", precoFileDuplo1
            print "total a pagar eh de R$ ", totalApagar
            print "valor desc Cartao Tabajara R$ ", valorDescCart
            print "total a pagar com desconto R% ", totalApagar - valorDescCart
 
        if qty1 > 5 and (tipoPagamento == "N" or tipoPagamento == "n"):
            totalApagar = precoFileDuplo2*qty1
            print "\npreco por KG eh de R$", precoFileDuplo2
            print "total a pagar eh de R%", totalApagar
        if qty1 > 5 and (tipoPagamento == "S" or tipoPagamento == "s"):
            totalApagar = precoFileDuplo2*qty1
            valorDescCart = totalApagar*descCartao
            print "\npreco por KG eh de R$ ", precoFileDuplo2
            print "total a pagar eh de R$ ", totalApagar
            print "valor desc Cartao Tabajara R$ ", valorDescCart
            print "total a pagar com desconto R% ", totalApagar - valorDescCart
 
    if tipo1 == "A" or tipo1 == "a":
        if qty1 <= 5 and (tipoPagamento == "N" or tipoPagamento == "n"):
            totalApagar = precoAlcatra1*qty1
            print "\npreco por KG eh de R$", precoAlcatra1
            print "total a pagar eh de R%", totalApagar
        if qty1 <= 5 and (tipoPagamento == "S" or tipoPagamento == "s"):
            totalApagar = precoAlcatra1*qty1
            valorDescCart = totalApagar*descCartao
            print "\npreco por KG eh de R$ ", precoAlcatra1
            print "total a pagar eh de R$ ", totalApagar
            print "valor desc Cartao Tabajara R$ ", valorDescCart
            print "total a pagar com desconto R% ", totalApagar - valorDescCart
 
        if qty1 > 5 and (tipoPagamento == "N" or tipoPagamento == "n"):
            totalApagar = precoAlcatra2*qty1
            print "\npreco por KG eh de R$", precoAlcatra2
            print "total a pagar eh de R%", totalApagar
        if qty1 > 5 and (tipoPagamento == "S" or tipoPagamento == "s"):
            totalApagar = precoAlcatra2*qty1
            valorDescCart = totalApagar*descCartao
            print "\npreco por KG eh de R$ ", precoAlcatra2
            print "total a pagar eh de R$ ", totalApagar
            print "valor desc Cartao Tabajara R$ ", valorDescCart
            print "total a pagar com desconto R% ", totalApagar - valorDescCart
 
    if tipo1 == "P" or tipo1 == "p":
        if qty1 <= 5 and (tipoPagamento == "N" or tipoPagamento == "n"):
            totalApagar = precoPicanha1*qty1
            print "\npreco por KG eh de R$", precoPicanha1
            print "total a pagar eh de R%", totalApagar
        if qty1 <= 5 and (tipoPagamento == "S" or tipoPagamento == "s"):
            totalApagar = precoPicanha1*qty1
            valorDescCart = totalApagar*descCartao
            print "\npreco por KG eh de R$ ", precoPicanha1
            print "total a pagar eh de R$ ", totalApagar
            print "valor desc Cartao Tabajara R$ ", valorDescCart
            print "total a pagar com desconto R% ", totalApagar - valorDescCart
 
        if qty1 > 5 and (tipoPagamento == "N" or tipoPagamento == "n"):
            totalApagar = precoPicanha2*qty1
            print "\npreco por KG eh de R$", precoPicanha2
            print "total a pagar eh de R%", totalApagar
        if qty1 > 5 and (tipoPagamento == "S" or tipoPagamento == "s"):
            totalApagar = precoPicanha2*qty1
            valorDescCart = totalApagar*descCartao
            print "\npreco por KG eh de R$ ", precoPicanha2
            print "total a pagar eh de R$ ", totalApagar
            print "valor desc Cartao Tabajara R$ ", valorDescCart
            print "total a pagar com desconto R% ", totalApagar - valorDescCart
 
    if tipo2 == "F" or tipo2 == "f":
        if qty1 <= 5 and (tipoPagamento == "N" or tipoPagamento == "n"):
            totalApagar2 = precoFileDuplo1*qty1
            print "\npreco por KG eh de R$", precoFileDuplo1
            print "total a pagar eh de R%", totalApagar2
        if qty1 <= 5 and (tipoPagamento == "S" or tipoPagamento == "s"):
            totalApagar2 = precoFileDuplo1*qty1
            valorDescCart = totalApagar2*descCartao
            print "\npreco por KG eh de R$ ", precoFileDuplo1
            print "total a pagar eh de R$ ", totalApagar2
            print "valor desc Cartao Tabajara R$ ", valorDescCart
            print "total a pagar com desconto R% ", totalApagar2 - valorDescCart
 
        if qty1 > 5 and (tipoPagamento == "N" or tipoPagamento == "n"):
            totalApagar2 = precoFileDuplo2*qty1
            print "\npreco por KG eh de R$", precoFileDuplo2
            print "total a pagar eh de R%", totalApagar2
        if qty1 > 5 and (tipoPagamento == "S" or tipoPagamento == "s"):
            totalApagar2 = precoFileDuplo2*qty1
            valorDescCart = totalApagar2*descCartao
            print "\npreco por KG eh de R$ ", precoFileDuplo2
            print "total a pagar eh de R$ ", totalApagar2
            print "valor desc Cartao Tabajara R$ ", valorDescCart
            print "total a pagar com desconto R% ", totalApagar2 - valorDescCart
 
    if tipo2 == "A" or tipo2 == "a":
        if qty1 <= 5 and (tipoPagamento == "N" or tipoPagamento == "n"):
            totalApagar2 = precoAlcatra1*qty1
            print "\npreco por KG eh de R$", precoAlcatra1
            print "total a pagar eh de R%", totalApagar2
        if qty1 <= 5 and (tipoPagamento == "S" or tipoPagamento == "s"):
            totalApagar2 = precoAlcatra1*qty1
            valorDescCart = totalApagar2*descCartao
            print "\npreco por KG eh de R$ ", precoAlcatra1
            print "total a pagar eh de R$ ", totalApagar2
            print "valor desc Cartao Tabajara R$ ", valorDescCart
            print "total a pagar com desconto R% ", totalApagar2 - valorDescCart
 
        if qty1 > 5 and (tipoPagamento == "N" or tipoPagamento == "n"):
            totalApagar2 = precoAlcatra2*qty1
            print "\npreco por KG eh de R$", precoAlcatra2
            print "total a pagar eh de R%", totalApagar2
        if qty1 > 5 and (tipoPagamento == "S" or tipoPagamento == "s"):
            totalApagar2 = precoAlcatra2*qty1
            valorDescCart = totalApagar2*descCartao
            print "\npreco por KG eh de R$ ", precoAlcatra2
            print "total a pagar eh de R$ ", totalApagar2
            print "valor desc Cartao Tabajara R$ ", valorDescCart
            print "total a pagar com desconto R% ", totalApagar2 - valorDescCart
 
    if tipo2 == "P" or tipo2 == "p":
        if qty1 <= 5 and (tipoPagamento == "N" or tipoPagamento == "n"):
            totalApagar2 = precoPicanha1*qty1
            print "\npreco por KG eh de R$", precoPicanha1
            print "total a pagar eh de R%", totalApagar2
        if qty1 <= 5 and (tipoPagamento == "S" or tipoPagamento == "s"):
            totalApagar2 = precoPicanha1*qty1
            valorDescCart = totalApagar2*descCartao
            print "\npreco por KG eh de R$ ", precoPicanha1
            print "total a pagar eh de R$ ", totalApagar2
            print "valor desc Cartao Tabajara R$ ", valorDescCart
            print "total a pagar com desconto R% ", totalApagar2 - valorDescCart
 
        if qty1 > 5 and (tipoPagamento == "N" or tipoPagamento == "n"):
            totalApagar2 = precoPicanha2*qty1
            print "\npreco por KG eh de R$", precoPicanha2
            print "total a pagar eh de R%", totalApagar2
        if qty1 > 5 and (tipoPagamento == "S" or tipoPagamento == "s"):
            totalApagar2 = precoPicanha2*qty1
            valorDescCart = totalApagar2*descCartao
            print "\npreco por KG eh de R$ ", precoPicanha2
            print "total a pagar eh de R$ ", totalApagar2
            print "valor desc Cartao Tabajara R$ ", valorDescCart
            print "total a pagar com desconto R% ", totalApagar2 - valorDescCart