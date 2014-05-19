#coding: utf-8
import datetime, time
from eventos import *
from provas import *

class Participante_BBB:
    
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
    evento1 = Eventos("Divisao de Grupos", apresentador, "Dividindo Grupos")
    evento2 = Eventos("Divisao de Lados", apresentador, "Dividindo Lados")
    evento3 = Eventos("Festas", apresentador, "Festas Semanais")
    evento4 = Eventos("BigFone", apresentador, "Evento do Big Fone")
    evento5 = Eventos("Prova do Dinheiro", apresentador, "Evento do Dinheiro")
    evento6 = Eventos("Prova da Compra", apresentador, "Evento da Compra")
    evento7 = Eventos("Fazer Compras", apresentador, "Evento das Compras")
    prova1 = Provas("Prova do Líder", "Prova da Liderança", "Definir um Líder da Semana" )
    print dir(evento1)
    print dir(prova1)
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
        participante = Participante_BBB(nome, cidade, idade, estalecas, grupo, lado)
        participante.inscreveParticipante()
        participante.apresentaParticipante()
        part = [participante.nome, participante.cidade, participante.idade, participante.estalecas, participante.grupo, participante.lado]
        listaParticipante.append(part)
 
    event1 = evento1.divisaoGrupos(listaParticipante)
    event2 = evento2.divisaoLados(listaParticipante, week)
    event3 = evento3.festas(week)
    event4 = evento4.bigFone(week, listaParticipante)
    event5 = evento5.provaDinheiro(n)
    event6 = evento6.provaCompra(n, estalecas)
    event7 = evento7.fazerCompras(week, listaParticipante)
    prov1 = prova1.defineLider(week, listaParticipante)

    print "Apresentando o Programa\n Lista de Participantes\n", listaParticipante, "\n" 
    print "Apresentador\n", apresentador , "\n"
    print "Duracao do Evento \n", duracao, "\n"
    print "Essas são as Festas do Programa! \n", event3, "\n"
    print "Essa é a Prova do Líder", prova1, "\n"
            














    

# data = "2008-08-12"
# ndata = time.strptime(data, "%Y-%m-%d")
# ndata = datetime.datetime(*ndata[0:5])
# print ndata.strftime('%d/%m/%Y')
# # "12/08/2008"
# print "Daqui a duas semanas sera " + ( ndata - datetime.timedelta(weeks=+2)
    