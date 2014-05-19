#coding: utf-8

import random

class Provas:
    
    lider = None #nome do lider
    nome = None #nome do evento
    objetivo = None #nome do apresentador do evento
    descricao = None #descricao do evento
    
    def __init__(self, nome, objetivo, descricao):
        self.nome = nome
        self.objetivo = objetivo
        self.descricao = descricao             
    
    def defineLider(self, week, listaParticipante):
        for i in range(week):
            self.lider = random.choice(listaParticipante)
            print "Este é o Líder da Semana\n", self.lider, "\n"    
    