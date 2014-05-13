#coding: utf-8

# Problem Set "Project"
# Fonte: http://www.python.org.br/wiki/ListaDeExercicios
# Name: Matheus Felix

def conversao(num):
    return ((num/1024)/1024)

def percentual(lista,num):    
    return ((float(num)*100)/sum(lista))

def ordenar(lista):
    return lista.sort()

f=open("usuarios.txt","r")
lista = f.readlines()
print lista
f.close()

result="ACME Inc.               Uso do espaço em disco pelos usuários\n"
result+="----------------------------------------------------------------\n"
result+="Nr.\tUsuário\t\tEspaço utilizado\t% do uso\n"    
    
listaUsuario=[]
listaEspaco=[]
listaUtilizacao=[]

for i in lista:
    listaUsuario.append(i[0:16])
    print listaUsuario, "LISTA USUARIO"
    listaEspaco.append(conversao(int(i[16:])))
    print listaEspaco, "Lista Espaco"
    
print listaEspaco, "lista espaco espaco"
print sorted(listaEspaco), "Sort Lista Espaco"


for i in range (len(listaUsuario)):
    listaUtilizacao.append(percentual(listaEspaco, listaEspaco[i]))
    print listaUtilizacao.append(percentual(listaEspaco, listaEspaco[i])), "Print AQUI"
    print listaUtilizacao, "Print aqui 2"
    result += str(i+1) + "\t" + listaUsuario[i]  +  str("%.2f" %(listaEspaco[i])) + "\tMB" + "\t\t" + str("%.2f" %(listaUtilizacao[i])) + "\n"
    
print listaUtilizacao , "lista lista lista"

# result += str(i+1) + "\t" + listaUsuario[i]  +  str("%.2f" %(listaEspaco[i])) + 
# "\tMB" + "\t\t" + str("%.2f" %(listaUtilizacao[i])) + "\n"

print str("%.2f" %(listaEspaco[i])), "Lista1 Lista2"
print (result)    

f=open("teste.html", "w")
f.write(result)
f.close()

