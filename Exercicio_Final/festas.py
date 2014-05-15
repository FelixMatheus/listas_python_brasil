#coding: utf-8

from Exercicio_Python import Apresentacao
import datetime, time

class Festas(object):
    i = 0
    fest = []
    festas = []
    for i in range(Apresentacao.week):
        Festa = raw_input("Digite nome da Festa: ")
        Apr_Festa = raw_input("Digite um Apresentador: ")
        fest = [(Festa, Apr_Festa)]
        festas.append(fest)
    print "Essas São as Festas da Semana Inicial Até a Final\n", festas