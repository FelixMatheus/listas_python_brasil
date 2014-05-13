#coding: utf-8
#TESTE DO EXERCICIO ACME LISTA 9 UTILIZANDO JSON

import json
 
nr=[]
nome=""
utilizado=[]
res=[]
result=[]
a=[]

with open("usuarios.json", "w") as usuarios:
    usuario = {}
    usuario['nr'] = 'nr'
    usuario['nome'] = 'nome'
    usuario['utilizado'] = 'utilizado'
    usuarios.write(json.dumps(usuario))
      
i = 0    
contato = {}
  
with open("usuarios.json", "a") as usuarios:
    while (i == 0):
        n = input ("Digite o Numero de Usuarios: ")
        nr = []
        nome = []
        utilizado = []
        uso = 0
        u2 = ' MB'
        soma = 0
        for i in range(n):
            nr.append(int(input("Digite um Numero de Usuario: ")))
            nome.append(raw_input("Digite um Nome de Usuario: "))
            utilizado.append((((int(input("Digite o Espaço Utilizado: "))/1024)/1024)))
#         for item in utilizado:
#             soma += item
#             uso = ((utilizado)*100/soma)
#         media = soma / len(utilizado)
#         print "Media %d \n" % media
#         print uso, "uso"
#         u3 = (float(utilizado)*100/media)       
        u1 = [str(nr) + str(nome) + str(utilizado) + '' ,'' + str(u2)]
        result += u1
        print result
        usuario['result'] = result
#         result += "\n"+ nr + "\t" +  nome + "\t" + utilizado
        usuario['nr'] = int(nr)
        usuario['nome'] = str(nome)
        usuario['utilizado'] = int(utilizado)
        
        usuarios.write(json.dumps(usuario))
          
        if (nome=="sair"):
            i = 1