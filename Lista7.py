#coding: utf-8

#"Estrutura Sequencial"
#Fonte: http://www.python.org.br/wiki/ListaDeExercicios
#Name: Matheus Felix

#Exercicio Extra 1 (json)

import json
  
nome=""
result=""
with open("contatos.json", "w") as contatos:
    contato = {}
    contato['nome'] = 'nome'
    contato['tel'] = 'tel'
    contatos.write(json.dumps(contato))
      
i = 0    
contato = {}
  
with open("contatos.json", "a") as contatos:
    while (i == 0):
        nome = raw_input("Digite o nome: ")
        tel = raw_input ("Digite o tel: ")
        result += "\n"+ nome + "\t" +  tel
        contato['nome'] = str(nome)
        contato['tel'] = str(tel)
        contatos.write(json.dumps(contato))
          
        if (nome=="sair"):
            i = 1

 
#Exercicio Extra 1 (txt)
 
nome=""
result=""
while (nome!="sair"):
    nome = raw_input("Digite o nome: ")
    if (nome=="sair"):
        break
    tel = raw_input ("Digite o tel: ")
    result += "\n"+ nome + "\t" +  tel
      
f=open("contatos.txt","w")
f.write("Nome\tTelefone" + result)
f.close()
 
#Exercicio Extra 2
 
f=open("contatos.txt","r")
 
lista = f.readlines()
for i in lista:
    print (i)
f.close()

#Exercicio Extra 3

tipo=""
result=""
while (tipo!="sair"):
    tipo = raw_input("Digite o tipo do navio: ")
    if (tipo=="sair"):
        break
    latitude = raw_input("Digite a Latitude: ")
    longitude = raw_input("Digite a Longitude: ")
    hora = raw_input ("Digite a hora: ")
    result += "\n"+ tipo + "\t" +  latitude + "\t\t" + longitude + "\t\t" + hora
 
print ("Navio\tLatitude\tLongitude\tHora" + result)
 
f=open("frota.txt","w")
f.write("Navio\tLatitude\tLongitude\tHora" + result)
f.close()

#Exercicio Extra 4

f=open("frota.txt", "r")
 
lista = f.readlines()
for i in lista:
        print(i)
f.close()

#Exercicio 1 (Python Brasil)

f=open("ip.txt","r")
lista = f.readlines()
f.close()
 
ipvalido = ""
ipnaovalido = ""
 
for i in range (len(lista)):
    print len(lista), "TAMANHO DA LISTA"
    lista2 = lista[i].rsplit(".")
    print lista2 , "LISTA 2"
    if (int(lista2[0])<=255 and int(lista2[1])<=255 and int(lista2[2])<=255 and int(lista2[3])<=255):
        ipvalido += lista[i] + "\n"
        print ipvalido , "IPVALIDO"
    else:
        ipnaovalido += lista[i] + "\n"
        print ipnaovalido, "IPNAOVALIDO"
 
f=open("ipvalido.txt","w")
f.write(ipvalido)
f.close()
 
f=open("ipnaovalido.txt","w")
f.write(ipnaovalido)
f.close()
    
#Exercicio 2 Python Brasil

def conversao(num):
    return ((num/1024)/1024)

def percentual(lista,num):    
    return ((float(num)*100)/sum(lista))

f=open("usuarios.txt","r")
lista = f.readlines()
f.close()

result="ACME Inc.               Uso do espaço em disco pelos usuários\n"
result+="----------------------------------------------------------------\n"
result+="Nr.\tUsuário\t\tEspaço utilizado\t% do uso\n"    
    
listaUsuario=[]
listaEspaco=[]
listaUtilizacao=[]

for i in lista:
    listaUsuario.append(i[0:16])
    listaEspaco.append(conversao(int(i[16:])))

for i in range (len(listaUsuario)):
    listaUtilizacao.append(percentual(listaEspaco, listaEspaco[i]))
    result += str(i+1) + "\t" + listaUsuario[i]  +  str("%.2f" %(listaEspaco[i])) + "\tMB" + "\t\t" + str("%.2f" %(listaUtilizacao[i])) + "\n"

print (result)    
    
    

