#coding: utf-8
import datetime, time

class bbb:
    
    nome = None
    cidade = None
    idade = None #varia de 22 a 40 anos
    estalecas = None
    dataInicio = None #começa num domingo
    duracao = None #duracao em semanas do programa
    grupo = None
    lado = None
    
    def __init__(self, nome, cidade, idade, estalecas, grupo, lado):
        self.nome = nome
        self.cidade = cidade
        self.idade = idade
        self.estalecas = estalecas
        self.grupo = grupo
        self.lado = lado
              
    def inscreveParticipante(self):
        return self.nome, self.cidade, self.idade, self.estalecas, self.grupo, self.lado
        
    def apresentaParticipante(self):
        print self.nome, self.cidade, self.idade, self.estalecas, self.grupo, self.lado
                    
class Apresentacao(object):
    n = 4 #Numero de Participantes
    apresentador = raw_input("Digite o Nome do Apresentador: ")
    i = 0
    grupo = ""
    lado = ""
    listaParticipante = []
    dataInicio = "2014-01-05"
    dataInicio = time.strptime(dataInicio, "%Y-%m-%d")
    dataInicio = datetime.datetime(*dataInicio[0:5])
    week = n-1 #Duracao do Evento mediante ao numero de participantes
    duracao = ( dataInicio + datetime.timedelta(weeks=+week))
    for i in range(n):
        nome = raw_input("Digite um nome: ")
        cidade = raw_input("Digite uma cidade: ")
        idade = int(input("Digite uma idade: "))
        estalecas = 0 #Estalecas Iniciais
        participante = bbb(nome, cidade, idade, estalecas, grupo, lado)
        participante.inscreveParticipante()
        participante.apresentaParticipante()
        part = [participante.nome, participante.cidade, participante.idade, participante.estalecas, participante.grupo, participante.lado]
        listaParticipante.append(part)

   
    print "Apresentando o Programa\n Lista de Participantes\n", listaParticipante, "\n" 
    print "Apresentador\n", apresentador , "\n"
    print "Duracao do Evento \n", duracao, "\n"
    



        
        
            














    

# data = "2008-08-12"
# ndata = time.strptime(data, "%Y-%m-%d")
# ndata = datetime.datetime(*ndata[0:5])
# print ndata.strftime('%d/%m/%Y')
# # "12/08/2008"
# print "Daqui a duas semanas sera " + ( ndata - datetime.timedelta(weeks=+2)
    