#coding: utf-8

from Exercicio_Python import Apresentacao

import random

class Paredao:
    lider = None
    anjo = None
    paredao_1 = None
    paredao_2 = None
    a = "" 
    b = "" 
    c= ""  
    d= ""
    
    
    def inscreveParedao(self):
        self.lider = random.choice(Apresentacao.listaParticipante)
        self.anjo = random.choice(Apresentacao.listaParticipante)
        self.paredao_1 = random.choice(Apresentacao.listaParticipante)
        self.paredao_2 = random.choice(Apresentacao.listaParticipante)
        print self.lider, self.anjo, self.paredao_1, self.paredao_2
        print self.lider[0], self.anjo[0], self.paredao_1[0], self.paredao_2[0]
        a = self.lider[0]
        print a
        b = self.anjo[0]
        print b
        c = self.paredao_1[0]
        print c
        d = self.paredao_2[0]
        print d
        if a==b:
            while a==b:
                b = random.choice(Apresentacao.listaParticipante)
                e = b[0]
        else:
            print b
            if b==c or b==d:
                while b==c or b==d:
                    c = random.choice(Apresentacao.listaParticipante)
                    f = c[0]
            else:
                print c
                if c==d or c==a:
                    while c==d or c==a or c==b:
                        d = random.choice(Apresentacao.listaParticipante)
                        g = d[0]
                else:
                    print d
        
        print a, b, c, d, "Print hereeeeeeeeeeee"
        print e, f, g , "Print here"
        return a, b, c, d, e, f, g
                   
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

#     def inscreveParedao(self):
#         self.lider = random.choice(Apresentacao.listaParticipante)
#         self.anjo = random.choice(Apresentacao.listaParticipante)
#         self.paredao_1 = random.choice(Apresentacao.listaParticipante)
#         self.paredao_2 = random.choice(Apresentacao.listaParticipante)
#         print self.anjo
#         print self.lider
#         if not self.lider==Apresentacao.listaParticipante[0] and not self.lider==Apresentacao.listaParticipante[1] and not self.lider==Apresentacao.listaParticipante[2] and not self.lider==Apresentacao.listaParticipante[3]:
#             print self.anjo
#         else:
#             self.anjo = random.choice(Apresentacao.listaParticipante)
#             print self.anjo
#         if not self.lider==Apresentacao.listaParticipante[0] and not self.lider==Apresentacao.listaParticipante[1] and not self.lider==Apresentacao.listaParticipante[2] and not self.lider==Apresentacao.listaParticipante[3] and not self.anjo==Apresentacao.listaParticipante[0] and not self.anjo==Apresentacao.listaParticipante[1] and not self.anjo==Apresentacao.listaParticipante[2] and not self.anjo==Apresentacao.listaParticipante[3]:
#             print self.paredao_1
#         else:
#             self.paredao_1 = random.choice(Apresentacao.listaParticipante)
#             print self.paredao_1
#         if not self.lider==Apresentacao.listaParticipante[0] and not self.lider==Apresentacao.listaParticipante[1] and not self.lider==Apresentacao.listaParticipante[2] and not self.lider==Apresentacao.listaParticipante[3] and not self.anjo==Apresentacao.listaParticipante[0] and not self.anjo==Apresentacao.listaParticipante[1] and not self.anjo==Apresentacao.listaParticipante[2] and not self.anjo==Apresentacao.listaParticipante[3] and not self.paredao_1==Apresentacao.listaParticipante[0] and not self.paredao_1==Apresentacao.listaParticipante[1] and not self.paredao_1==Apresentacao.listaParticipante[2] and not self.paredao_1==Apresentacao.listaParticipante[3]:
#             print self.paredao_2
#         else:
#             self.paredao_2 = random.choice(Apresentacao.listaParticipante)
#             print self.paredao_2
#         return self.lider, self.anjo, self.paredao_1, self.paredao_2


#        if self.lider[0]!=self.anjo[0]:
#             while self.lider[0]!=self.anjo[0]:
#                 self.anjo=random.choice(Apresentacao.listaParticipante)
#                 anjo1 = self.anjo
#                 print anjo1, "Anjo Aqui"
#         else:
#             while self.lider[0]!=self.anjo[0]:
#                 self.anjo=random.choice(Apresentacao.listaParticipante)
#                 anjo1 = self.anjo
#                 print anjo1 , "Anjo Novo"
#                 
#         if self.lider[0]!=self.anjo[0] and self.anjo[0]!=self.paredao_1[0]:
#             while self.lider[0]!=self.anjo[0] and self.anjo[0]!=self.paredao_1[0]:
#                 self.paredao_1 = random.choice(Apresentacao.listaParticipante)
#                 pared_1 = self.paredao_1
#                 print pared_1, "Pared 1" 
#         else:
#             while self.lider[0]!=self.anjo[0] and self.anjo[0]!=self.paredao_1[0]:
#                 self.paredao_1 = random.choice(Apresentacao.listaParticipante)
#                 pared_1 = self.paredao_1
#                 print pared_1, "Pared 1"      
#                 
#         if self.lider[0]!=self.anjo[0] and self.anjo[0]!=self.paredao_1[0] and self.paredao_1[0]!=self.paredao_2[0]:
#             while self.lider[0]!=self.anjo[0] and self.anjo[0]!=self.paredao_1[0] and self.paredao_1[0]!=self.paredao_2[0]:
#                 self.paredao_2 = random.choice(Apresentacao.listaParticipante)
#                 pared_2 = self.paredao_2
#                 print pared_2, "Pared 2"
#         else:
#             while self.lider[0]!=self.anjo[0] and self.anjo[0]!=self.paredao_1[0] and self.paredao_1[0]!=self.paredao_2[0]:
#                 self.paredao_2 = random.choice(Apresentacao.listaParticipante)
#                 pared_2 = self.paredao_2
#                 print pared_2, "Pared 2"