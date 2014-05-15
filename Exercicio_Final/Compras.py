#coding: utf-8

from Exercicio_Python import Apresentacao
from ProvaDinheiro import ProvaDinheiro

import random

class ProvaCompra(object):
    N_Estalecas = []
    for i in range(Apresentacao.n):
        Apresentacao.estalecas = Apresentacao.estalecas + 2000 + ProvaDinheiro.NProvaDinheiro
        N_Estalecas = [Apresentacao.estalecas]
    print N_Estalecas
   
class Compra(object):
    ProvaCompra = ProvaCompra()
    leite = 25
    margarina = 100
    pao = 10
    queijo = 100
    Pagar = []
    qtd_Leite = 0
    qtd_Margarina = 0
    qtd_Pao = 0
    qtd_Queijo = 0
    quem_fez = ""
    for i in range(Apresentacao.week):
        qtd_Leite = int(input("Digite Quantidade Leite: "))
        qtd_Margarina = int(input("Digite Quantidade Margarina: "))
        qtd_Pao = int(input("Digite Quantidade Pao: "))
        qtd_Queijo = int(input("Digite Quantidade Queijo: "))
        
        Qtd_Semanal = (qtd_Leite + qtd_Margarina + qtd_Pao + qtd_Queijo)
        Pagar = (qtd_Leite*leite) + (qtd_Margarina*margarina) + (qtd_Pao*pao) + (qtd_Queijo*queijo)
        
        if Pagar <= ProvaCompra: 
            print Pagar, "Pagou esse valor pela Compra da Semana"
            print Qtd_Semanal, "Quantidade Semanal\n"
            print qtd_Leite, "Numero de Leites Semanais"
            print qtd_Margarina, "Numero de Margarinas Semanais"
            print qtd_Pao, "Numero de Pãos Semanais"
            print qtd_Queijo, "Numero de Queijos Semanais\n"
                
        if qtd_Leite>4 and qtd_Margarina>1 and qtd_Pao>30 and qtd_Queijo>2:
            print "Custo do Café da Manha Semanal\n"
            qtd_Leite = qtd_Leite - 1
            qtd_Margarina = qtd_Margarina -1
            qtd_Pao = qtd_Pao - 1
            qtd_Queijo = qtd_Queijo - 1
            Qtd_Nova = (qtd_Leite + qtd_Margarina + qtd_Pao + qtd_Queijo)
            print Qtd_Nova, "Sobraram essa Quantidade Total de Produtos\n"
            quem_fez = random.choice(Apresentacao.listaParticipante)
            print quem_fez , "Esse Participante fez o café da manhã da Semana\n"
        
        
            
            


        
        
