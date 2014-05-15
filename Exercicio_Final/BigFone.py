#coding: utf-8

from Exercicio_Python import Apresentacao
import random

class BigFone(object):
    quem_atende = ""
    missoes = ['Coma Todo cafe da manha', 'Nao tome cafe', 'Seja Anjo', 'Seja Lider']
    for i in range(Apresentacao.week):
        BigFone = random.choice(missoes)
        quem_atende = random.choice(Apresentacao.listaParticipante)
        print "Missão do Big Fone", BigFone 
        print "Quem Atendeu?\n", quem_atende 
    