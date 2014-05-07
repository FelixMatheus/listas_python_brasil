# Problem Set "Estrutura de Repetição"
# Fonte: http://www.python.org.br/wiki/ListaDeExercicios
# Name: Matheus Felix

#Exercicio 1

nota = input("digite uma nota de 0 a 10: ")
while 0 > nota or 10 < nota:
    nota = input("digite uma nota de 0 a 10: ")             

#Exercicio 2

user = raw_input("Usuario: ")
senha = raw_input("Senha: ")

if (user != senha):
    print "ok"
else: 
    user = raw_input("Usuario: ")
    senha = raw_input("Senha: ")
    
#Exercicio 3

nome = "d"
while len(nome) <= 3:
    nome = raw_input("digite seu nome ---> ")
 
idade = -1
while idade < 0 or idade > 150:
    idade = input("digite sua idade ---> ")
 
salario = 0
while salario <= 0:
    salario = input("digite seu salario ---> ")
 
sexo = "p"
while sexo != "f" and sexo != "m":
    sexo = raw_input("digite seu sexo m - masculino ou f - feminino ---> ")
 
estadoCivil = "n"
while estadoCivil != "s" and estadoCivil != "c" and estadoCivil != "v" and estadoCivil != "d":
    estadoCivil = raw_input("digite seu estado civil s - solteiro, c - casado, v - viuvo ou d = divorciado ---> ")
    
#Exercicio 4

populacaoA = 80000
populacaoB = 200000
taxaCrescA = 0.03
taxaCrescB = 0.015
 
anos = 1
while populacaoA < populacaoB:
    populacaoA = populacaoA*(1 + taxaCrescA)
    populacaoB = populacaoB*(1 + taxaCrescB)
    anos = anos + 1
 
print "Populacao A: ", round(populacaoA)
print "Populacao B: ", round(populacaoB)
print "Anos: ", anos

#Exercicio 5

finalizar = "n"
while finalizar == "n":
 
    populacaoA = input("digite a populacao A: ")
    populacaoB = input("digite a populacao B: ")
    taxaCrescA = input("digite a taxa de crescimento populacao A (ex: 0.1 para 10%: ")
    taxaCrescB = input("digite a taxa de crescimento populacao B (ex: 0.1 para 10%: ")
 
    anos = 1
    while populacaoA < populacaoB:
        populacaoA = populacaoA*(1 + taxaCrescA)
        populacaoB = populacaoB*(1 + taxaCrescB)
        anos = anos + 1
 
    print "Populacao A: ", round(populacaoA)
    print "Populacao B: ", round(populacaoB)
    print "Anos: ", anos
 
    finalizar = raw_input("deseja sair do programa? s - sim ou n - nao ")
    
#Exercicio 6

i = 1
while i < 21:
    print(i)
    i = i + 1
 
i = 1
while i < 21:
    print(i),
    i = i + 1

#Exercicio 9

i = 1
while i < 50:
    if i%2 != 0:
        print(i)
    i = i + 1
    
#Exercicio 10

soma = 0
number1 = input("digite um numero inteiro ---> ")
number2 = input("digite outro numero inteiro ---> ")
if number1 < number2:
    while number1 < number2:
        number1 = number1 + 1        
        soma = soma + number1
        if number1 < number2:
            print(number1)
 
elif number2 < number1:
    while number2 < number1:
        number2 = number2 + 1
        soma = soma + number2
        if number2 < number1:
            print(number2)
                        
#Exercicio 11

soma = 0
number1 = input("digite um numero inteiro: ")
number2 = input("digite outro numero inteiro: ")
if number1 < number2:
    while number1 < number2:
        number1 = number1 + 1        
        soma = soma + number1
        if number1 < number2:
            print(number1)
    soma = soma - number2
elif number2 < number1:
    while number2 < number1:
        number2 = number2 + 1
        soma = soma + number2
        if number2 < number1:
            print(number2)
    soma = soma - number1
 
print "soma dos numeros dentro do intervalo = ", soma

#Exercicio 12

tabuadaDe = input("digite o numero da tabuada que deseja visualizar (1 a 10): ")
 
i = 1
while i < 11:
    print tabuadaDe, " X ",i," = ", tabuadaDe*i
    i = i + 1
    
#Exercicio 13

base = input("digite a base: ")
expoente = input("digite o expoente: ")
baseCalc = 1
i = 0
while i < expoente:
    baseCalc = baseCalc*base
    i = i + 1
print base," ^ ",expoente," = ",baseCalc

#Exercicio 14

par = 0
impar = 0
i = 1
while i < 11:
    numero = input("digite um numero: ")
    if numero%2 == 0:
        par = par + 1
    else:
        impar = impar + 1
    i = i + 1
 
print "dos 10 numeros digitados, ",par," sao par e ",impar," sao impar"

#Exercicio 15

n = input("digite o numero de termos que desea formar da serie de fibonacci: ")
 
i = 1
a = 0
b = 1
print(b)
while i < n:
    c = a + b
    print(c)
    a = b
    b = c
    i = i + 1
    
#Exercicio 16

i = 1
a = 0
b = 1
c = 0 
print(b)
while c < 500:
    c = a + b
    print(c)
    a = b
    b = c
    i = i + 1
    
#Exercicio 17

numero = input("digite um numero para calcularmos o seu fatorial ---> ")
numeroCalc = numero
fatorial = 1
while numeroCalc > 0:
    fatorial = fatorial*numeroCalc
    numeroCalc = numeroCalc - 1   
print "fatorial de ", numero, " = ", fatorial

#Exercicio 18

 
qtyNum = input("quantos numeros deseja avaliar? ")
soma = 0
i = 0
while i < qtyNum:
    numero = input("digite um numero: ")
    if i == 0:
        menor = numero
        maior = numero
    else:
        if numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero
    soma = soma + numero   
    i = i + 1
print "a soma dos numeros eh igual a: ", soma
print "o maior numero eh: ", maior
print "o menor numero eh: ", menor

#===============================================================================
# #Exercicio 16
# 
#  
# termos = input("digite o numero de termos da serie ---> ")
#  
# soma = 0
# fatDem = 1
# i = 1
# while i <= termos:
#     soma = soma + (float(i)/fatDem)
#     print(soma)
#     fatDem = fatDem + 2
#     i = i + 1
#     
# #Exercicio 17
# 
# termos = input("digite o numero de termos da serie ---> ")
#  
# soma = 0
# i = 1
# while i <= termos:
#     soma = soma + (1/float(i))
#     print(soma)
#     i = i + 1
#       
# #Exercicio 19
# 
# termos = input("digite o numero de termos da serie ---> ")
#  
# soma = 0
# fatNum = 1
# i = 1
# while i <= termos:
#     soma = soma + (fatNum/float(i))
#     print " + ", fatNum, "/", i, 
#     #print(soma)
#     fatNum = fatNum + 2
#     i = i + 1
# print " = ", soma
#===============================================================================



#Exercicio 25
#===============================================================================
# 
# qtyNum = input("quantos numeros deseja avaliar? ---> ")
# soma = 0
# i = 0
# while i < qtyNum:
#     numero = input("digite um numero entre 0 e 65536 ---> ")
#     while (numero < 0) or (numero > 65536):
#         numero = input("o numero deve ser entre  0 e 65536 !!! ---> ")
#     if i == 0:
#         menor = numero
#         maior = numero
#     else:
#         if numero > maior:
#             maior = numero
#         elif numero < menor:
#             menor = numero
#     soma = soma + numero   
#     i = i + 1
# print "a soma dos numeros eh igual a ---> ", soma
# print "o maior numero eh ---> ", maior
# print "o menor numero eh ---> ", menor
#===============================================================================

#Exercicio 19

#Exercicio 20

numero = raw_input("digite um numero (0 a 16) para calcularmos o seu fatorial ou digite sair para sair: ")
while numero != "sair":
    numeroCalc = int(numero)
    fatorial = 1
    while numeroCalc > 0:
        fatorial = fatorial*numeroCalc
        numeroCalc = numeroCalc - 1   
    print "fatorial de ", numero, " = ", fatorial
    numero = raw_input("digite um numero (0 a 16) para calcularmos o seu fatorial ou digite sair para sair: ")
      
#Exercicio 21

numero = input("digite um numero: ")
i = 2

if numero != 2: 
    while i < numero:
        if numero%i == 0:
            justify = i
            verify = 0
            i = numero
        else:
            i = i + 1
            verify = 1        
        if verify == 1:
            print numero, " eh primo"
        else:
            print numero, " nao eh primo pois eh divisivel por ", justify
else:
        print numero, "eh primo"
        
#Exercicio 23

n = input("digite um numero: ")
primeTest = 5
divisao = 0
 
while primeTest < n:
    i = 2
    v = 0
    while i < primeTest:
        resto = primeTest%i
        divisao = divisao + 1
        if resto == 0:
            i = primeTest
            v = 0
        if resto !=0:
            i = i + 1
            v = 1
    if v == 1:
        print i, "primo\n "
    primeTest = primeTest + 1
    
print divisao, "divisoes"

#Exercicio 24

n = float(input("digite um numero de notas que deseja: "))
 
i = 0
soma = 0
float(soma)

while i < n:
    nota = float(input("digite a nota: "))
    soma = soma + nota
    i = i + 1
    
media = soma / i
float(media)
print "media igual a: ", media

#Exercicio 25

n = input("digite um numero de idades que deseja inputar: ")
 
i = 0
soma = 0
while i < n:
    idade = input("digite a idade: ")
    soma = soma + idade
    i = i + 1
    
media = soma / i
print "media de idade igual a: ", media

if media <=25:
    print("turma jovem")
elif 25 < media <= 60:
    print("turma adulta")
elif media > 60:
    print("turma idosa")
    
#Exercicio 26

n = input("digite o numero de votantes: ")
 
i = 0
soma1 = 0
soma2 = 0
soma3 = 0
while i < n:
    voto = input("digite 1 para o candidato1, 2 para o candidato2, 3 para o candidato3: ")
    if voto == 1:
        soma1 = soma1 + 1
    elif voto == 2:
        soma2 = soma2 + 1
    elif voto == 3:
        soma3 = soma3 + 1
    i = i + 1
print "Candidato 1 teve: ", soma1, "votos"
print "Candidato 2 teve: ", soma2, "votos"
print "Candidato 3 teve: ", soma3, "votos"

#Exercicio 27

n = input("digite o numero de turmas: ")
 
i = 0
soma = 0
 
while i < n:
    alunosPorTurmas = input("digite o numero de alunos da turma: ")
    if (alunosPorTurmas) < (41):
        soma = soma + alunosPorTurmas
        i = i + 1
        media = soma / i
    else:
        print "Número de alunos maior que 40!"
        
print "media de alunos por turma: ", float(media)

#Exercicio 29

i = 1
while i < 51:
    print i, " - R$", i*1.99
    i = i + 1
   
#Exercicio 30

precoPao = input("digite o preco do pao ---> ")
print "preco do pao ---> R$", float(precoPao)
print("Panificadora Pão de Ontem - Tabela de preços")
i = 1
while i < 51:
    print i, " - R$", i*precoPao
    i = i + 1

#Exercicio 31

fim = 1
while fim !=0:
    soma = 0
    i = 1
    valor = input("digite o valor do produto ou 0 para finalizar ---> ")
    while valor > 0:
        soma = soma + valor
        print "Produto ",i,": R$ ", float(valor)
        i = i + 1
        valor = input("digite o valor do produto ou 0 para finalizar ---> ")
 
    if soma > 0:
        print "Total --> R$", soma
        formaPagamento = input("Forma de pagamento - digite 1 para cheque ou 2 para dinheiro ---> ")
        if formaPagamento == 2:
            qtyDinheiro = input("Informe o valor pago ---> ")
            troco = qtyDinheiro - soma
        else:
            troco = 0
        print "troco de R$", troco
        troco = 0
    fim = input("digite 0 para sair ou 1 para continuar -> ")
    
#Exercicio 32

numero = input("digite um numero para calcularmos o seu fatorial: ")
numeroCalc = numero
fatorial = 1
print "Fatorial de",numero,":"
print numero,"! = ",
while numeroCalc > 0:
    fatorial = fatorial*numeroCalc
    if numeroCalc > 1:
        print numeroCalc," . ",
    else:
        print numeroCalc,
    numeroCalc = numeroCalc - 1   
 
print " = ",fatorial

#Exercicio 33

i = 1
soma = 0
a = 0
 
tempEntrada = raw_input("digite uma temperatura ou digite \"sair\" sem aspas para sair: ")
maiorTemp = tempEntrada
menorTemp = tempEntrada
 
if tempEntrada == "sair":
    tempEntrada = tempEntrada
    a = tempEntrada
else:
    tempEntrada = float(int(tempEntrada))
 
while a != "sair":    
    if tempEntrada > maiorTemp:
        maiorTemp = tempEntrada
    else:
        tempEntrada = tempEntrada
    if tempEntrada < menorTemp:
        menorTemp = tempEntrada
    else:
        menorTemp = menorTemp
 
    soma = soma + tempEntrada
 
    tempEntrada = raw_input("digite uma temperatura ou digite \"sair\" sem aspas para sair ---> ")
    if tempEntrada == "sair":
        tempEntrada = tempEntrada
        a = tempEntrada
    else:
        tempEntrada = float(int(tempEntrada))    
        i = i + 1
 
if i > 0:      
    media = soma / i
    print i, "i"
    print "maior temperatura = ", maiorTemp,"graus"
    print "menor temperatura = ", menorTemp,"graus"
    print "soma das temperaturas = ", soma,"graus"
    print "media temperatura = ", media,"graus"

#Exercicio 34

#Exercicio 35

#Exercicio 36

comeco = 10
fim = 1
tabuadaDe = 1
while comeco >= fim:
    tabuadaDe = input("digite o numero da tabuada que deseja visualizar (1 a 10) ---> ")
    comeco = input("digite o numero que a tabuada deve comecar (1 a 10) ---> ")
    fim = input("digite o numero que a tabuada deve terminar (1 a 10) ---> ")
 
print "\nMontar a tabuada de: ", tabuadaDe
print "Comecar por: ", comeco
print "Terminar por:", fim
 
while comeco < (fim+1):
    print tabuadaDe, " X ",comeco," = ", tabuadaDe*comeco
    comeco = comeco + 1


#===============================================================================
# i = 0
# maiorNumero = 0
# while i < 5:
#     numero = input("digite um numero ---> ")
#     if numero > maiorNumero:
#         maiorNumero = numero
#     else:
#         maiorNumero = maiorNumero
#     i = i + 1
# print "maior numero digitado foi ---> ", maiorNumero
#===============================================================================

#Exercicio 37

altura = input("\ndigite sua altura em metros ---> ")
peso = input ("digite seu peso em kg ---> ")
code = input ("digite seu codigo ---> ")
saida = input("digite 1 para continuar ou 0 para sair ---> ")
 
maiorAltura = altura
maiorAlturaCode = code
menorAltura = altura
menorAlturaCode = code
maiorPeso = peso
maiorPesoCode = code
menorPeso = peso
menorPesoCode = code
somaAltura = altura
somaPeso = peso
i = 0
 
while saida != 0:
    altura = input("\ndigite sua altura em metros ---> ")
    peso = input ("digite seu peso em kg ---> ")
    code = input ("digite seu codigo ---> ")
    saida = input("digite 1 para continuar ou 0 para sair ---> ")
 
    if altura > maiorAltura:
        maiorAltura = altura
        maiorAlturaCode = code
    else:
        maiorAltura = maiorAltura
 
    if altura < menorAltura:
        menorAltura = altura
        menorAlturaCode = code
    else:
        menorAltura = menorAltura
 
    if peso > maiorPeso:
        maiorPeso = peso
        maiorPesoCode = code
    else:
        maiorPeso = maiorPeso
 
    if peso < menorPeso:
        menorPeso = peso
        menorPesoCode = code    
    else:
        menorPeso = menorPeso
 
    somaAltura = somaAltura + altura
    somaPeso = somaPeso + peso
    i = i + 1
 
if i != 0:
    mediaPeso = float(somaPeso) / (i + 1)
    mediaAltura = float(somaAltura) / (i + 1)
    print menorPeso, "kg pesa o mais magro, code ---> ",menorPesoCode
    print maiorPeso, "kg pesa o mais gordo, code ---> ",maiorPesoCode
    print menorAltura, "m mede o mais baixo, code ---> ",menorAlturaCode
    print maiorAltura, "m mede o mais alto, code ---> ",maiorAlturaCode
    print mediaPeso, "kg eh a media de peso da academia"
    print mediaAltura, "m eh a media de altura da academia"
 

#Exercicio 38

anoInicial = input("digite o ano que foi contratado ---> ")
salario = input("digite seu salario em R$ ---> ")
anoFinal = input("digite o ultimo ano de contrato ---> ")
ajuste = 0.015
anoInicial = anoInicial + 1
i = 1
 
while anoInicial <= anoFinal:
    if anoInicial <= 1995 or i ==1:
        ajuste = ajuste
    else:
        ajuste = ajuste*2
    salario = salario + salario*ajuste 
    print anoInicial, " - ajuste de -->",ajuste*100,"% -- Salario ajustado de R$",salario
    anoInicial = anoInicial + 1
    i = i + 1
    
#Exercicio 39

numero = input("digite o numero do aluno: ")
altura = input("digite a altura do aluno: ")
maiorAltura = altura
maiorAlturaNumero = numero
menorAltura = altura
menorAlturaNumero = numero
 
i = 1
while i < 3:
    numero = input("\ndigite o numero do aluno: ")
    altura = input("digite a altura do aluno: ")
 
    if altura > maiorAltura:
        maiorAltura = altura
        maiorAlturaNumero = numero
 
    if altura < menorAltura:
        menorAltura = altura
        menorAlturaNumero = numero 
    i = i + 1
 
print "\nnumero do aluno mais baixo: ", menorAlturaNumero, " -- ", menorAltura,"metros"
print "numero do aluno mais alto: ", maiorAlturaNumero, " -- ", maiorAltura,"metros"

#Exercicio 40

#Exercicio 41

divida = float(input("\nDigite o valor da divida R$ "))
juros = 0.00
print("Valor da Dívida##Valor dos Juros ## Quantidade de Parcelas##Valor da Parcela")
print "R$",divida," ",juros*100,"%",1,"R$",divida
 
i = 3
while i < 13:
    juros = juros + 0.05
    print "R$",divida," ",juros*100,"%",i,"R$",(divida/i)+(divida/i)*juros
    i = i + 3
    
#Exercicio 40

i = 0
soma = 0
while i < 5:
    numero = input("digite um numero ---> ")
    soma = soma + numero
    i = i + 1
 
media = float(soma)/i
print "soma dos numeros digitados ---> ", soma
print "media dos numeros digitados ---> ", media


    
#Exercicio 43

n = input("digite um numero para ter todos os primos menores que ele ---> ")
print(1)
print(2)
print(3)
primeTest = 5
while primeTest < n:
    i = 2
    v = 0
    while i < primeTest:
        resto = primeTest%i
        if resto == 0:
            i = primeTest
            v = 0
        if resto !=0:
            i = i + 1
            v = 1
    if v == 1:
        print i
    primeTest = primeTest + 1
       
#Exercicio 46

anoInicial = input("digite o ano que foi contratado ---> ")
salario = input("digite seu salario em R$ ---> ")
anoFinal = input("digite o ultimo ano de contrato ---> ")
ajuste = 0.015
anoInicial = anoInicial + 1
i = 1
 
while anoInicial <= anoFinal:
    if anoInicial <= 1995 or i ==1:
        ajuste = ajuste
    else:
        ajuste = ajuste*2
    salario = salario + salario*ajuste 
    print anoInicial, " - ajuste de -->",ajuste*100,"% -- Salario ajustado de R$",salario
    anoInicial = anoInicial + 1
    i = i + 1
    
#Exercicio 48

codigoCidade = input("digite o codigo da cidade ---> ")
qtyVeiculos = input("digite numero de veiculos da cidade ---> ")
qtyAcidentes = input("digite numero de acidentes com vitimas da cidade ---> ")
indiceAcidente = float(qtyAcidentes)/qtyVeiculos
maiorIndice = indiceAcidente
maiorIndiceCode = codigoCidade
menorIndice = indiceAcidente
menorIndiceCode = codigoCidade
soma = qtyVeiculos
somaVeiculos2000 = 0
divisorMedia2000 = 1
if qtyVeiculos < 2000:
    somaVeiculos2000 = somaVeiculos2000 + qtyAcidentes
    divisorMedia2000 = divisorMedia2000 + 1
 
i = 1
while i < 3:
    codigoCidade = input("digite o codigo da cidade ---> ")
    qtyVeiculos = input("digite numero de veiculos da cidade ---> ")
    qtyAcidentes = input("digite numero de acidentes com vitimas da cidade ---> ") 
    indiceAcidente = float(qtyAcidentes)/qtyVeiculos
    soma = soma + qtyVeiculos
 
    if indiceAcidente > maiorIndice:
        maiorIndice = indiceAcidente
        maiorIndiceCode = codigoCidade
 
    if indiceAcidente < menorIndice:
        menorIndice = indiceAcidente
        menorIndiceCode = codigoCidade
 
    if qtyVeiculos < 2000:
        somaVeiculos2000 = somaVeiculos2000 + qtyAcidentes
        divisorMedia2000 = divisorMedia2000 + 1
 
    i = i + 1
 
print "\nmenor indice ---> ", menorIndice, " -- codigo da cidade ---> ", menorIndiceCode 
print "maior indice ---> ", maiorIndice, " -- codigo da cidade ---> ", maiorIndiceCode
print "media de veiculos nas,",i,"cidades = ", float(soma)/i," veiculos"
print "media de acidentes em cidades com menos de 2000 veiculos --->", float(somaVeiculos2000)/divisorMedia2000

#Exercicio 49

divida = float(input("\nDigite o valor da divida R$ ---> "))
juros = 0.00
print("Valor da Dívida##Valor dos Juros##Quantidade de Parcelas##Valor da Parcela")
print "R$",divida,"           ",juros*100,"%          ",1,"          R$",divida
 
i = 3
while i < 13:
    juros = juros + 0.05
    print "R$",divida,"           ",juros*100,"%          ",i,"          R$",(divida/i)+(divida/i)*juros
    i = i + 3
    
#Exercicio 50

numero = 0
entre0e25 = 0
entre26e50 = 0
entre51e75 = 0
entre76e100 = 0
i = 0 
while numero >=0:
    numero = input("digite um numero positivo (para sair digite um numero negativo) ---> ")
    if 0 <= numero <= 25:
        entre0e25 = entre0e25 + 1
    elif 26 <= numero <= 50:
        entre26e50 = entre26e50 + 1
    elif 51 <= numero <= 75:
        entre51e75 = entre51e75 + 1
    elif 76 <= numero <= 100:
        entre76e100 = entre76e100 + 1
 
print entre0e25, "numeros no intervalo [0-25]"
print entre26e50, "numeros no intervalo [26-50]"
print entre51e75, "numeros no intervalo [51-75]"
print entre76e100, "numeros no intervalo [76-100]"

#Exercicio 51

print "Especificação   Código  Preço"
print "Cachorro Quente 100     R$ 1,20"
print "Bauru Simples   101     R$ 1,30"
print "Bauru com ovo   102     R$ 1,50"
print "Hambúrguer      103     R$ 1,20"
print "Cheeseburguer   104     R$ 1,30"
print "Refrigerante    105     R$ 1,00\n"
 
valor = 0
soma = 0
i = 1
codigo = 1
while codigo != 0:
    codigo = input("digite o codigo do produto ou 0 para sair ---> ")
    if codigo != 0:
        qty = input("digite a quantidade do produto ---> ")
 
        if codigo == 100:
            valor = 1.2
 
        elif codigo == 101:
            valor = 1.3
 
        elif codigo == 102:
            valor = 1.5
 
        elif codigo == 103:
            valor = 1.2
 
        elif codigo == 104:
            valor = 1.3
 
        elif codigo == 105:
            valor = 1.0
 
        valorParcial = valor*qty
        print codigo," -- ",qty," --- R$",valorParcial
        soma = soma + valorParcial
if soma != 0:
    print "valor total ---> R$", soma

#Exercicio 52

print "Vote de acordo com os seguintes codigos:\n\n1 - Joao \n2 - Jose \n3 - Marcos \n4 - Eneas \n5 - Voto Nulo \n6 - Voto em Branco\n ----------> digite 0 para sair"
 
voto = 1
soma = 0
soma1 = 0
soma2 = 0
soma3 = 0
soma4 = 0
soma5 = 0
soma6 = 0
 
while voto != 0:
    voto = input("digite o codigo do seu voto ---> ")
    if voto == 1:
        soma1 = soma1 + 1
 
    elif voto == 2:
        soma2 = soma2 + 1
 
    elif voto == 3:
        soma3 = soma3 + 1
 
    elif voto == 4:
        soma4 = soma4 + 1
 
    elif voto == 5:
        soma5 = float(soma5 + 1)
 
    elif voto == 6:
        soma6 = float(soma6 + 1)
 
    soma = soma + 1 #total de votos
 
print soma1,"votos para o Joao\n",soma2,"votos para Jose\n",soma3,"votos para Marcos\n",soma4,"votos para Eneas\n",soma5,"votos Nulos\n",soma5,"votos em Branco\n",(soma5/soma)*100,"% votos nulos\n",(soma6/soma)*100,"% votos brancos"

#Exercicio 45

#Gabarito
gab01 = "A"
gab02 = "B"
gab03 = "C"
gab04 = "D"
gab05 = "E"
gab06 = "E"
gab07 = "D"
gab08 = "C"
gab09 = "B"
gab10 = "A"
 
#fim do gabarito
soma = 0
maiorAcerto = -1
menorAcerto = 11
final = 1
i = 1
somaMedia = 0
 
while final == 1:
    resposta01 = raw_input("digite a resposta da questao 1 ---> ")
    if resposta01 == gab01:
        soma = soma + 1
 
    resposta02 = raw_input("digite a resposta da questao 2 ---> ")
    if resposta02 == gab02:
        soma = soma + 1
 
    resposta03 = raw_input("digite a resposta da questao 3 ---> ")
    if resposta03 == gab03:
        soma = soma + 1
 
    resposta04 = raw_input("digite a resposta da questao 4 ---> ")
    if resposta04 == gab04:
        soma = soma + 1
 
    resposta05 = raw_input("digite a resposta da questao 5 ---> ")
    if resposta05 == gab05:
        soma = soma + 1
 
    resposta06 = raw_input("digite a resposta da questao 6 ---> ")
    if resposta06 == gab06:
        soma = soma + 1
 
    resposta07 = raw_input("digite a resposta da questao 7 ---> ")
    if resposta07 == gab07:
        soma = soma + 1
 
    resposta08 = raw_input("digite a resposta da questao 8 ---> ")
    if resposta08 == gab08:
        soma = soma + 1
 
    resposta09 = raw_input("digite a resposta da questao 9 ---> ")
    if resposta09 == gab09:
        soma = soma + 1
 
    resposta10 = raw_input("digite a resposta da questao 10 ---> ")
    if resposta10 == gab10:
        soma = soma + 1
 
    if soma > maiorAcerto:
        maiorAcerto = soma
 
    if soma < menorAcerto:
        menorAcerto = soma
 
    somaMedia = float(somaMedia + soma)
 
    final = input("para outro aluno responder a prova, digite 1, para finalizar digite 0 ---> ")
    i = i + 1
    soma = 0
 
print "maior numero de acertos ---> ", maiorAcerto,"acertos"
print "menor numero de acertos ---> ", menorAcerto,"acertos"
print "alunos usaram o sistema ---> ",(i-1)
print "media das notas da turma", somaMedia/(i-1)

#Exercicio 54

numero = input("digite um numero inteiro positivo ---> ")
numeroStr = str(numero)
i = len(numeroStr)
 
while i >= 0:
    print numeroStr[i - 1: i],
    i = i - 1


