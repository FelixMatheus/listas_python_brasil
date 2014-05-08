# Problem Set "Listas"
# Fonte: http://www.python.org.br/wiki/ListaDeExercicios
# Name: Matheus Felix

#Exercicio 1

vetorList = [2, 3, 5, 7, 11]
 
i = 0
while i < len(vetorList):
    print(vetorList[i])
    i = i + 1

#Exercicio 2

vetorList = [2, 3, 5, 7, 11, 4, 6, 8, 9, 10]
 
i = 1
while i <= len(vetorList):
    print vetorList[len(vetorList) - i]
    i = i + 1
    
#Exercicio 3

notasList = [6.0, 7.0, 5.0, 8.0]
i = 0
soma = 0
while i < len(notasList):
    print "Nota",i+1,"---> ", notasList[i]
    soma = soma + notasList[i]
    i = i + 1
print "media ---> ", soma/len(notasList)

#Exercicio 3

nL = [1,2,3,4,5]
sm = 0
for item in nL:
    sm += item
md = sm/len(nL)
print "media", md

#Exercicio 4

letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
 
i = 0
soma = 0
vetorConsoantes = []
while i < len(letras):
    if letras[i] != "a" and letras[i] != "e" and letras[i] != "i" and letras[i] != "o" and letras[i] != "u":
        soma = soma + 1
        vetorConsoantes.append(letras[i])
    i = i + 1
print "numero de consoantes", soma
 
i = 0
while i < len(vetorConsoantes):
    print vetorConsoantes[i],
    i = i + 1

#Exercicio 5

i = 0
vetor = []
vetorImpar = []
vetorPar = []
 
while i < 20:
    numero = input("digite um numero: ")
    vetor.append(numero)
    if numero%2 == 0:
        vetorPar.append (numero)
    else:
        vetorImpar.append (numero)
    i = i + 1
 
print "todos os numeros digitados: ", vetor
print "vetor de numeros impares: ", vetorImpar
print "vetor de numeros pares: ", vetorPar

#Exercicio 6

vetorMedias = []
i = 0
while i < 20:
    print "digite as 4 notas do aluno numero ", i+1
    e = 0
    soma = 0
    while e < 4:
        nota = input("digite sua nota: ")
        soma = soma + float(nota)
        e = e + 1
    media = soma/4
    vetorMedias.append(media)
    i = i + 1
    print "\n\n"
 
somaAlunos = 0
b = 0
while b < len(vetorMedias):
    if vetorMedias > 7.0:
        somaAlunos = somaAlunos + 1
    b = b + 1
 
print "numero de alunos com  media maior que 7.0 ", somaAlunos

#Exercicio 7

vetorNumeros = [5, 4, 3, 8, 7]
 
soma = 0
multiplica = 1
i = 0
while i < len(vetorNumeros):
    soma = soma + vetorNumeros[i]
    multiplica = multiplica*vetorNumeros[i]
    i = i + 1
 
print "multiplicacao dos numeros do vetor ", multiplica
print "soma dos numeros do vetor ", soma
print "vetor ", vetorNumeros

#Exercicio 8

vetorIdade = []
vetorAltura = []
i = 0
while i < 5:
    idade = input("digite sua idade: ")
    altura = input("digite sua altura em metros: ")
    vetorIdade.append(idade)
    vetorAltura.append(altura)
    i = i + 1
 
vetorIdade.reverse()
print "vetor idade ", vetorIdade
vetorAltura.reverse()
print "vetor altura ", vetorAltura

#Exercicio 9

vetorNumeros = [1, 5, 3, 4, 8, 13, 17, 2, 9, 20]
somaQuadrados = 0
i = 0
while i < len(vetorNumeros):
    somaQuadrados = somaQuadrados + vetorNumeros[i]*vetorNumeros[i]
    i = i + 1
 
print "soma dos quadrados dos elementos do vetor: ", somaQuadrados

#Exercicio 10

vetorA = [1, 2 , 3, 4, 5, 6, 7, 8, 9, 10]
vetorB = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
vetorC = []
i = 0
while i < len(vetorA):
    vetorC.append(vetorA[i])
    vetorC.append(vetorB[i])
    i = i + 1
 
print "vetor resultado: ", vetorC

#Exercicio 11

vetorA = [1, 2 , 3, 4, 5, 6, 7, 8, 9, 10]
vetorB = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
vetorC = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
vetorD = []
 
i = 0
while i < len(vetorA):
    vetorD.append(vetorA[i])
    vetorD.append(vetorB[i])
    vetorD.append(vetorC[i])
    i = i + 1
 
print "vetor resultado: ", vetorD

#Exercicio 12

idades = [14, 12, 13, 16, 18, 20, 13]
alturas = [1.8, 1.9, 1.0, 2.0, 1.4, 1.3, 1.85]
soma = 0
 
somaAltura = 0
a = 0
while a < len(alturas):
    somaAltura = somaAltura + alturas[a]
    a = a + 1
 
media = somaAltura/(len(alturas))
 
i = 0
while i < len(idades):
    if idades[i]>13 and alturas[i] < media:
        soma = soma + 1
    i = i + 1
 
print "alunos com altura abaixo da media ---> ", soma

#Exercicio 13

mesesStr = ["janeiro", "fevereiro", "marco", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
tempAno = []
 
i = 0
while i < 12:
    print "\nmes de "+mesesStr[i]  
    tempMes = input("digite a temperatura do mes: ")
    tempAno.append(tempMes)
    i = i + 1
 
somaTemp = 0
i = 0
while i < len(tempAno):
    somaTemp = somaTemp + tempAno[i]
    i = i + 1
 
mediaTemp = somaTemp/len(tempAno)
 
print "\nmedia anual de temperatura: ", mediaTemp,"graus\nMeses com temperatura acima da media anual:"
soma = 0
i = 0
while i < len(tempAno):
    if tempAno[i] > mediaTemp:
        print mesesStr[i]," - ",tempAno[i]," graus"
        soma = soma + 1
    i = i + 1
 
if soma == 0:
    print "nunhum mes teve temperatura acima da media anual"

#Exercicio 14

print "responda sim ou não\n"
 
perguntas = ["Telefonou para a vítima? ---> ", "Esteve no local do crime? ---> ", "Mora perto da vítima? ---> ", "Devia para a vítima? ---> ", "Já trabalhou com a vítima? ---> "]
 
soma = 0
i = 0
while i < len(perguntas):
    resp = raw_input(perguntas[i])
    if resp == "sim":
        soma = soma + 1
    else:
        soma = soma
    i = i + 1
 
if soma < 2:
    print "voce eh inocente!"
elif soma == 2:
    print "voce eh suspeito!"
elif 4<= soma <= 5:
    print "voce eh cumplice!"
elif soma == 5:
    print "voce eh o assassino!!"

#Exercicio 15

valores = [0]
valoresUpMedia = []
valoresDown7 = []
 
while valores[len(valores)-1] != (-1):
    print "\npara sair digite -1"
    valor = input("digite um numero ---> ")
    valores.append(valor)
 
valores.pop(0)
valores.pop(len(valores)-1)
 
print "\nquantidade de valores lidos ---> ",len(valores)
 
print "valores lidos ---> ", 
 
soma = 0
i = 0
while i < len(valores):
    soma = soma + valores[i]
    if valores[i] < 7:
        valoresDown7.append(valores[i])
    print valores[i],
    i = i + 1
 
media = soma/len(valores)
i = 0
while i < len(valores):
    if valores[i] > media:
        valoresUpMedia.append(valores[i])
    i = i + 1
 
print "\nsoma dos valores lidos ---> ",soma
print "media dos valores lidos ---> ", media
print "quantidade de valores acima da media ---> ", len(valoresUpMedia)
print "quantidade de valores abaixo de 7 ---> ", len(valoresDown7)
print "\n\nAte a proxima execucao!!!!"

#Exercicio 16

#Exercicio 17

posicaoSaltos = ["Primeiro", "Segundo", "Terceiro", "Quarto", "Quinto"]
 
saltos = []
nome = raw_input("\ndigite o nome do atleta (digite sair para sair) ---> ")
while nome != "sair":
    i = 0
    soma = 0
    print "Atleta : "+nome+"\n"
    while i < 5:
        print posicaoSaltos[i],
        distSalto = input(" Salto ---> ")
        saltos.append(distSalto)
        soma = soma + distSalto
        i = i + 1
    media = soma / len(saltos)
    print "\nResultado Final:"
    print "Atleta: "+nome
    a = 0
    while a < len(saltos)-1:
        print saltos[a]," - ",
        a = a + 1
    print saltos[len(saltos)-1]
    print "Media dos saltos: ",media,"m"
    nome = raw_input("\ndigite o nome do atleta (digite sair para sair) ---> ")
    
#Exercicio 18

votos = [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0]
 
print "Enquete: Quem foi o melhor jogador?"        
 
i = 1
while i != 0:
    voto = input("Numero do jogador (0=fim)---> ")
    while voto < 0 or voto > 23:
        print "Informe um valor entre 1 e 23 ou 0 para sair!"
        voto = input("Numero do jogador (0=fim)---> ")
    if voto == 0:
        i = voto
    else:
        votos[voto - 1] = votos[voto - 1] + 1
        i = i
 
print "\nResultado da votacao"
 
i = 0
while i < len(votos):
    print "Camisa numero",(i+1),"--->",votos[i],"votos"
    i = i + 1
    
#Exercicio 19

print "Qual o melhor Sistema Operacional para uso em Servidores?\n\n"
print "As possiveis respostas sao: \n"
print "1- Windows XP\n2- Unix\n3- Linux\n4- Netware\n5- Mac Os\n6- Outro\nDigite 0 para sair\n"
 
votos = [1]
while votos[len(votos)-1] != 0:
    voto = input("digite seu voto ---> ")
    if voto <= 6 :
        votos.append(voto)
    else:
        print "Voto invalido, digite novamente"
 
votos.pop(0)
votos.pop(len(votos)-1)
 
votosWin = votos.count(1)
votosUni = votos.count(2)
votosLin = votos.count(3)
votosNet = votos.count(4)
votosMac = votos.count(5)
votosOut = votos.count(6)
 
total = votosWin + votosUni + votosLin + votosNet + votosMac + votosOut
 
porcWin = (float(votosWin)/(len(votos)))*100
porcUni = (float(votosUni)/(len(votos)))*100
porcLin = (float(votosLin)/(len(votos)))*100
porcNet = (float(votosNet)/(len(votos)))*100
porcMac = (float(votosMac)/(len(votos)))*100
porcOut = (float(votosOut)/(len(votos)))*100
print "-----------------------------------------------------" 
print "Sistema Operacional     Votos          Porcentagem"
print "Windows XP              ", votosWin,"    ","    ""%(#)0.2f%%" % {"#" : porcWin} 
print "Unix                    ", votosUni,"    ","    ""%(#)0.2f%%" % {"#" : porcUni}
print "Linux                   ", votosLin,"    ","    ""%(#)0.2f%%" % {"#" : porcLin}
print "Netware                 ", votosNet,"    ","    ""%(#)0.2f%%" % {"#" : porcNet}
print "Mac Os                  ", votosMac,"    ","    ""%(#)0.2f%%" % {"#" : porcMac}
print "Outtros                 ", votosOut,"    ","    ""%(#)0.2f%%" % {"#" : porcOut}
print "-----------------------------------------------------\n"
print "Total  ", total

#Exercicio 21

modelos = ["Fusca", "Variant", "Passat", "Corcel", "Fiat 147"]
consumoLitro = [0.5, 1, 3.5, 0.3, 33.5]
 
print "Comparativo de consumo de combustivel\n\n"
 
i = 0
while i < len(modelos):
    print "veiculo",(i+1)
    print "Nome: ", modelos[i]
    print "Km por litro: ", consumoLitro[i],"km/l\n\n"
    i = i + 1
 
print "Relatorio Final\n\n"
 
eco = 0
ecoIndice = 0
i = 0
while i < len(modelos):
    print (i+1)," - ",modelos[i]," - ",consumoLitro[i],"km/l - ",1000/consumoLitro[i]," litros - R$", 2.25*(1000/consumoLitro[i])
    if consumoLitro[i] > eco:
        eco = consumoLitro[i]
        ecoIndice = i
    i = i + 1
 
print "o carro mais economico eh o ",modelos[ecoIndice],"."

#Exercicio 22

defeitos = ["necessita da esfera", "necessita de limpeza", "necessita troca do cabo ou conector", "quebrado ou inutilizado"]
defeitosCount = [0, 0, 0, 0]
 
i = 1
while i != 0:
    print "1 - necessita da esfera\n2 - necessita de limpeza\n3 - necessita troca do cabo\n4 - ou conector quebrado ou inutilizado"
    defeito = input("Digite o numero referente ao defeito do mouse ou 0 para sair ---> ")
    if defeito != 0:
        defeitosCount[defeito-1] = defeitosCount[defeito-1] + 1 
    else:
        i = 0
 
i = 0
soma = 0
while i < len(defeitosCount):
    soma = soma + defeitosCount[i]
    i = i + 1
 
print "\n\nSituacao         Qty         Percentual"
 
i = 0
while i < len(defeitosCount):
    print (i + 1)," - "+defeitos[i]+"       ",defeitosCount[i],"        ",100*(float(defeitosCount[i])/soma),"%"
    i = i + 1