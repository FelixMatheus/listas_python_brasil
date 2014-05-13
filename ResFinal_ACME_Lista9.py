#coding: utf-8
#ACME PROJETO - 3 PRIMEIROS ITENS

def conversao(num):
    return ((num/1024)/1024)

def percentual(lista,num):    
    return ((float(num)*100)/sum(lista))

n = input("Defina número de Usuários que deseja imprimir: ")

f=open("usuarios.txt","r")
lista = f.readlines()
f.close()

print lista, "LISTAAAAAAAAAAAAAAA"

result="ACME Inc.               Uso do espaço em disco pelos usuários\n"
result+="----------------------------------------------------------------\n"
result+="Nr.\tUsuário\t\tEspaço utilizado\t% do uso\n"    
    
listaUsuario=[]
listaEspaco=[]
listaUtilizacao=[]

for i in lista:
    listaUsuario.append(i[0:16])
    listaEspaco.append(conversao(int(i[16:])))
    listaEspaco.sort()

for i in range (len(listaUsuario)):
    listaUtilizacao.append(percentual(listaEspaco, listaEspaco[i]))
    result += str(i+1) + "\t" + listaUsuario[i]  +  str("%.2f" %(listaEspaco[i])) + "\tMB" + "\t\t" + str("%.2f" %(listaUtilizacao[i])) + "\n"

print result

result1="ACME Inc.               Uso do espaço em disco pelos usuários\n"
result1+="----------------------------------------------------------------\n"
result1+="Nr.\tUsuário\t\tEspaço utilizado\t% do uso\n" 

for i in range (n):
    listaUtilizacao.append(percentual(listaEspaco, listaEspaco[i]))
    result1 += str(i+1) + "\t" + listaUsuario[i]  +  str("%.2f" %(listaEspaco[i])) + "\tMB" + "\t\t" + str("%.2f" %(listaUtilizacao[i])) + "\n"

print result1

f=open("teste.html","w")
f.write(result)
f.close()  

nr1=""
nome1=""
utilizado1=[]
uso1=""
saida=""
n2 = input("Digite Numero de Usuários que Deseja Imprimir: ")
for i in range(n2): 
    nr1 = raw_input("Digite o Numero: ")
    nome1 = raw_input("Digite o nome: ")
    utilizado1.append((int(input ("Digite o Espaço Utilizado: ")/1024)/1024))  
    saida += "\n"+ str(nr1) + "\t" + str(nome1) + "\t" +  "\t" + str(utilizado1)+"MB" + "\t\t\t" + str(uso1)

print saida 

f=open("usuarios1.txt","w")
f.write("ACME Inc.               Uso do espaço em disco pelos usuários\n----------------------------------------------------------------\nNr.\tUsuário\t\tEspaço utilizado\t% do uso\n" + saida)
f.close()




