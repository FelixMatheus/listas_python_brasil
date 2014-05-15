#coding: utf-8

from Exercicio_Python import Apresentacao
from festas import Festas
from Compras import ProvaCompra, Compra
from ProvaDinheiro import ProvaDinheiro
from BigFone import BigFone
from Divisao import Divisao

class ListaFinal(object):
    if not (Apresentacao.listaParticipante[0][4]):
        Apresentacao.listaParticipante[0][4] = 'Azul' 
        
    if not (Apresentacao.listaParticipante[1][4]):
        Apresentacao.listaParticipante[1][4] = 'Laranja'
         
    if not (Apresentacao.listaParticipante[2][4]):
        Apresentacao.listaParticipante[2][4] = 'Verde'
         
    if not (Apresentacao.listaParticipante[3][4]):
        Apresentacao.listaParticipante[3][4] = 'Vermelho'
    
    print "Essa é a Lista com os Grupos já divididos por Cores e Meia Competição\n", Apresentacao.listaParticipante 
    
    