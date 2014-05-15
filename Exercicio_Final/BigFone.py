#coding: utf-8

from Exercicio_Python import Apresentacao

import random

class BigFone(object):
    quem_atende = ""
    premio = ""
    prenda = ""
    BigFone = ""
    eae = ""
    missoes = ['[Coma Todo Cafe da manha]', '[Nao Tome Café]', '[Malhe Semana Inteira]', '[Pule na Piscina]']
    premio = ['[Moto]','[Carro]','[Celular]','[Notebook]','[Geladeira]']
    prenda = ['[Andar Descalço]','[Usar Peruca]','[Dormir na sala]','[Não Tomará Banho]']
    validacao = [True, False]
    for i in range(Apresentacao.week):
        BigFone = random.choice(missoes)
        quem_atende = random.choice(Apresentacao.listaParticipante)
        eae = random.choice(validacao)
        premio = random.choice(premio)
        prenda = random.choice(prenda)
        print "Missão do Big Fone -> ", BigFone 
        print "Quem Atendeu? -> ", quem_atende
        print "Efetuou a Missão? ->", eae, "\n"
        while eae == True:
            print "Parabens Você Ganhou um Prêmio!\n"
            print premio
            break
                
        while eae == False:
            print "Você será Obrigado a Pagar uma Prenda!"
            print prenda
            break
            