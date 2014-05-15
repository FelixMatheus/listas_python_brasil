#coding: utf-8

from Exercicio_Python import Apresentacao

import random

class Paredao:
    lider = None
    anjo = None
    paredao_1 = None
    paredao_2 = None
             
    def inscreveParedao(self):
        self.lider = random.choice(Apresentacao.listaParticipante)
        if not self.lider==Apresentacao.listaParticipante:
            self.anjo = random.choice(Apresentacao.listaParticipante)
        if not self.lider==Apresentacao.listaParticipante and not self.anjo==Apresentacao.listaParticipante:
            self.paredao_1 = random.choice(Apresentacao.listaParticipante)
        if not self.lider==Apresentacao.listaParticipante and not self.anjo==Apresentacao.listaParticipante and not self.paredao_1==Apresentacao.listaParticipante:
            self.paredao_2 = random.choice(Apresentacao.listaParticipante)
        return self.lider, self.anjo, self.paredao_1, self.paredao_2
    
class Semana(object):
    Lider = Paredao()
    print Lider.inscreveParedao()
    
# 
# class Anjo(object):
#     anjo = ""
#     Lider = Lider()
#     if not Lider==Apresentacao.listaParticipante:
# #    for i in range(Apresentacao.week):
#         anjo = random.choice(Apresentacao.listaParticipante)
#     print anjo
#     return anjo
# 
# class Paredao_1(object):
#     paredao_1 = ""
#     Lider=Lider()
#     Anjo=Anjo()
#     if not Lider==Apresentacao.listaParticipante and not Anjo==Apresentacao.listaParticipante:
#         paredao_1 = random.choice(Apresentacao.listaParticipante)
#     print paredao_1
#     return paredao_1
# 
# class Paredao_2(object):
#     paredao_2 = ""
#     Lider = Lider()
#     Anjo = Anjo()
#     Paredao_1 = Paredao_1()
#     if not Lider==Apresentacao.listaParticipante and not Anjo==Apresentacao.listaParticipante and not Paredao_1==Apresentacao.listaParticipante: 
#         paredao_2 = random.choice(Apresentacao.listaParticipante)
#     print paredao_2
#     return paredao_2
#         