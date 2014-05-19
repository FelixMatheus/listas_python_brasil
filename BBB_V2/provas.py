#coding: utf-8

import random

class Provas:
    
    lider = None #nome do lider
    anjo = None #nome do anjo
    imunizado = None #nome do imunizado
    nome = None #nome do evento
    objetivo = None #nome do apresentador do evento
    descricao = None #descricao do evento
    
    def __init__(self, nome, objetivo, descricao):
        self.nome = nome
        self.objetivo = objetivo
        self.descricao = descricao             
    
    def defineLider_Anjo_Imunizado_Paredao1(self, listaParticipante):
        
        print "Primeira Semana da Casa!\n"
        self.lider = random.choice(listaParticipante)
        listaParticipante.remove(self.lider)
        self.anjo = random.choice(listaParticipante)
        listaParticipante.remove(self.anjo)
        self.imunizado = random.choice(listaParticipante)
        listaParticipante.remove(self.imunizado)
        self.paredao_1 = random.choice(listaParticipante)
        print "Este é o Líder da Semana\n", self.lider, "\n"
        print "Esté o Anjo da Semana\n", self.anjo, "\n"
        print "Este é o Imunizado da Semana\n", self.imunizado, "\n"
        print "Este é o Sujeito do Paredão da Semana\n", self.paredao_1, "\n"
        
