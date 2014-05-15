#coding: utf-8

from Exercicio_Python import Apresentacao
from Festas import Festas
from Compras import ProvaCompra, Compra
from ProvaDinheiro import ProvaDinheiro
from BigFone import BigFone

class Eventos(object):
    if not (Apresentacao.listaParticipante[0][4]):
        Apresentacao.listaParticipante[0][4] = 'Azul' 
        print Apresentacao.listaParticipante[0][4]
    if not (Apresentacao.listaParticipante[1][4]):
        Apresentacao.listaParticipante[1][4] = 'Laranja'
        print Apresentacao.listaParticipante[1][4] 
    if not (Apresentacao.listaParticipante[2][4]):
        Apresentacao.listaParticipante[2][4] = 'Verde'
        print Apresentacao.listaParticipante[2][4] 
    if not (Apresentacao.listaParticipante[3][4]):
        Apresentacao.listaParticipante[3][4] = 'Vermelho'
        print Apresentacao.listaParticipante[3][4] 
    print Apresentacao.listaParticipante , "Essa é a Lista com os Grupos Definidos"
    
    