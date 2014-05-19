#coding: utf-8

import random

class Eventos:
    
    nome = None #nome do evento
    apresentador = None #nome do apresentador do evento
    descricao = None #descricao do evento
    NProvaDinheiro = None
    N_Estalecas = None
    
    def __init__(self, nome, apresentador, descricao):
        self.nome = nome
        self.apresentador = apresentador
        self.descricao = descricao
                
    def divisaoLados(self, listaParticipante, week):
        for i in range(week):
            listaParticipante[0][5] = 'Lado A'
            listaParticipante[1][5] = 'Lado A'
            listaParticipante[2][5] = 'Lado B'
            listaParticipante[3][5] = 'Lado B'
        return listaParticipante[0][5], listaParticipante[1][5], listaParticipante[2][5], listaParticipante[3][5]
    
    def divisaoGrupos(self, listaParticipante):
        if not (listaParticipante[0][4]):
            listaParticipante[0][4] = 'Azul' 
        
        if not (listaParticipante[1][4]):
            listaParticipante[1][4] = 'Laranja'
         
        if not (listaParticipante[2][4]):
            listaParticipante[2][4] = 'Verde'
         
        if not (listaParticipante[3][4]):
            listaParticipante[3][4] = 'Vermelho'
    
        return listaParticipante  
    
    def festas(self, week):
        i = 0
        fest = []
        festas = []
        for i in range(week):
            Festa = raw_input("Digite nome da Festa: ")
            Apr_Festa = raw_input("Digite um Apresentador: ")
            fest = [(Festa, Apr_Festa)]
            festas.append(fest)
        return festas
        
    def bigFone(self, week, listaParticipante):
        quem_atende = ""
        premio = ""
        prenda = ""
        BigFone = ""
        eae = ""
        missoes = ['[Coma Todo Cafe da manha]', '[Nao Tome Café]', '[Malhe Semana Inteira]', '[Pule na Piscina]']
        premio = ['[Moto]','[Carro]','[Celular]','[Notebook]','[Geladeira]']
        prenda = ['[Andar Descalço]','[Usar Peruca]','[Dormir na sala]','[Não Tomará Banho]']
        validacao = [True, False]
        for i in range(week):
            BigFone = random.choice(missoes)
            quem_atende = random.choice(listaParticipante)
            eae = random.choice(validacao)
            premio = random.choice(premio)
            prenda = random.choice(prenda)
            print "\nMissão do Big Fone -> ", BigFone 
            print "Quem Atendeu? -> ", quem_atende
            print "Efetuou a Missão? ->", eae, "\n"
            
            while eae == True:
                print "Parabens Você Ganhou um Prêmio!\n"
                print premio
                break
                  
            while eae == False:
                print "Você será Obrigado a Pagar uma Prenda!\n"
                print prenda
                break
            
        return BigFone, quem_atende, eae
    
    def provaDinheiro(self, n):
        Lista_Valores = [1500, 2000, 3000, 4000, 5000]
        for i in range(n):
            NProvaDinheiro = random.choice(Lista_Valores)
            self.NProvaDinheiro = NProvaDinheiro
    
    def provaCompra(self, n, estalecas):
        N_Estalecas = []
        for i in range(n):
            estalecas = str(estalecas) + str(2000) + str(self.NProvaDinheiro)
            N_Estalecas = [estalecas]
            self.N_Estalecas = N_Estalecas
        
    def fazerCompras(self, week, listaParticipante):
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
        for i in range(week):
            qtd_Leite = int(input("Digite Quantidade Leite: "))
            qtd_Margarina = int(input("Digite Quantidade Margarina: "))
            qtd_Pao = int(input("Digite Quantidade Pao: "))
            qtd_Queijo = int(input("Digite Quantidade Queijo: "))
            
            Qtd_Semanal = (qtd_Leite + qtd_Margarina + qtd_Pao + qtd_Queijo)
            Pagar = (qtd_Leite*leite) + (qtd_Margarina*margarina) + (qtd_Pao*pao) + (qtd_Queijo*queijo)
            
            if str(Pagar) <= str(self.N_Estalecas): 
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
                quem_fez = random.choice(listaParticipante)
                print quem_fez , "Esse Participante fez o café da manhã da Semana\n"
        return Qtd_Semanal, Pagar, quem_fez
            
