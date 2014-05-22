#coding: utf-8

import datetime, time
import random
import date

class Pessoa:
    
    nome = None
    cidade = None
    idade = None #varia de 22 a 40 anos
  
    def __init__(self, nome, cidade, idade):
        self.nome = nome
        self.cidade = cidade
        self.idade = idade
              
class Apresentador(Pessoa):
    Apresentador = Pessoa('Pedro Bial', 'RJ', '50')
        
class Edicao:
    dataInicio = "2014-01-05" #raw_input("Digite uma Data de Inicio em (Ano/Mes/Dia): ")
    dataInicio = time.strptime(dataInicio, "%Y-%m-%d")
    dataInicio = datetime.datetime(*dataInicio[0:5])
    Apresentador.Apresentador
    nro_edicao = "Quinta Edicao"
    nro_competidores = 6
    week = nro_competidores-2
    dataFim = (dataInicio + datetime.timedelta(weeks=+week))     

class Semana:
    semanas = Edicao.nro_competidores-2
    j = 0
    for j in range(semanas):
        j = j + 1
        
class Competidor(Pessoa):
    
    estalecas = 0
    grupo = None
    lado = None
    
    def __init__ (self, estalecas, grupo, lado):
        self.estalecas = estalecas
        self.grupo = grupo
        self.lado = lado
                   
    listaCompetidor = []
    grupo = ""
    for i in range(Edicao.nro_competidores):
            nome = raw_input("Digite o nome do Competidor: ")
            cidade = raw_input("Digite a cidade do Competidor: ")
            idade = raw_input("Digite a idade do competidor: ")
            comp = [nome, cidade, idade, estalecas, grupo, lado]
            listaCompetidor.append(comp)
            print listaCompetidor
 

class Eventos:
     
    nome = None #nome do evento
    apresentador = None #nome do apresentador do evento
    descricao = None #descricao do evento
    dataEvento = None #data do Evento
     
    def __init__(self, nome, apresentador, descricao, dataEvento):
        self.nome = nome
        self.apresentador = apresentador
        self.descricao = descricao
        self.dataEvento = dataEvento
        
class Grupo:
    if not (Competidor.listaCompetidor[0][4]):
            Competidor.listaCompetidor[0][4] = 'Azul' 
         
    if not (Competidor.listaCompetidor[1][4]):
            Competidor.listaCompetidor[1][4] = 'Laranja'
          
    if not (Competidor.listaCompetidor[2][4]):
            Competidor.listaCompetidor[2][4] = 'Verde'
          
    if not (Competidor.listaCompetidor[3][4]):
            Competidor.listaCompetidor[3][4] = 'Azul'
            
    if not (Competidor.listaCompetidor[4][4]):
            Competidor.listaCompetidor[4][4] = 'Laranja'
            
    if not (Competidor.listaCompetidor[5][4]):
            Competidor.listaCompetidor[5][4] = 'Verde'
 
class Competicao(Eventos):
    
    Competicao = ['Lados da Casa', 'Pedro Bial','Dividir em 2 lados', '2014-01-18'] 
    Competidor.listaCompetidor[0][5] = 'Lado A'
    Competidor.listaCompetidor[1][5] = 'Lado A'
    Competidor.listaCompetidor[2][5] = 'Lado A'
    Competidor.listaCompetidor[3][5] = 'Lado B'
    Competidor.listaCompetidor[4][5] = 'Lado B'
    Competidor.listaCompetidor[5][5] = 'Lado B'
    
    print Competicao, "\n"
    print Competidor.listaCompetidor, "Lista Atualizada com os Lados\n"
    
class Festas(Eventos):     
        festas = []
        for i in range(Edicao.week):
            nome = raw_input("Digite nome da Festa: ")
            apresentador = raw_input("Digite um Apresentador: ")
            descricao = 'Festa realizada dentro da Casa'
            dataEvento = date.randomDate("05-01-2014", "19-01-2014", random.random())
            fest = [(nome, apresentador, descricao, dataEvento)]
            festas.append(fest)
 
class BigFone(Eventos):
        dataFone = None
        bf = ['Big Fone!', 'BigBoss', "Realizar a Missao!", dataFone]
        quem_atendeu = ""
        premio1 = ""
        prenda1 = ""
        BigFone = ""
        eae = ""
        missoes = ['[Coma Todo Cafe da manha]', '[Nao Tome Café]', '[Malhe Semana Inteira]', '[Pule na Piscina]']
        premio = ['[Moto]','[Carro]','[Celular]','[Notebook]','[Geladeira]']
        prenda = ['[Andar Descalço]','[Usar Peruca]','[Dormir na sala]','[Não Tomará Banho]']
        validacao = [True, False]
        for i in range(Edicao.week):
            dataFone = date.randomDate("05-01-2014", "19-01-2014", random.random())
            BigFone = random.choice(missoes)
            quem_atendeu = random.choice(Competidor.listaCompetidor)
            eae = random.choice(validacao)
            premio1 = random.choice(premio)
            prenda1 = random.choice(prenda)
            print "\n", bf
            print "\nMissão do Big Fone -> ", BigFone 
            print "Quem Atendeu? -> ", quem_atendeu
            print "Efetuou a Missão? ->", eae, "\n"
               
            while eae == True:
                premio1
                print "Parabens Você Ganhou um Prêmio!"
                print premio1, "\n"
                break
                     
            while eae == False:
                prenda1
                print "Você será Obrigado a Pagar uma Prenda!"
                print prenda1, "\n"
                break
             
class Provas(Eventos):
     
    lider = None #nome do lider
    anjo = None #nome do anjo
    imunizado = None #nome do imunizado
    paredao_1 = None #nome do indicado 1
    vt_int = None #nome do indicado 2
    votos_internet = None
    votos_telefone = None
    indicado1 = None
    indicado2 = None
    objetivo = ""
          
    def provaDinheiro(self):
        Provas.objetivo = 'Prova do Dinheiro'
        Lista_Valores = [1500, 2000, 3000, 4000, 5000]
        for i in range(Edicao.nro_participantes):
            NProvaDinheiro = random.choice(Lista_Valores)
            self.NProvaDinheiro = NProvaDinheiro
            
      
    def provaCompra(self, estalecas):
        Provas.objetivo = 'Prova das Estalecas'
        N_Estalecas = []
        for i in range(Edicao.nro_participantes):
            estalecas = str(estalecas) + str(2000) + str(self.NProvaDinheiro)
            N_Estalecas = [estalecas]
            return N_Estalecas
      
    def defineLider_Anjo_Imunizado_Paredao1_VotInterna(self):
        Provas.objetivo = 'Definir Lider, Anjo, Imunizado, Indicado1, Indicado2 e Eliminado!'
        self.lider = random.choice(Competidor.listaCompetidor)
        Competidor.listaCompetidor.remove(self.lider)
        self.anjo = random.choice(Competidor.listaCompetidor)
        Competidor.listaCompetidor.remove(self.anjo)
        self.imunizado = random.choice(Competidor.listaCompetidor)
        Competidor.listaCompetidor.remove(self.imunizado)
        self.paredao_1 = random.choice(Competidor.listaCompetidor)
        Competidor.listaCompetidor.remove(self.paredao_1)
        self.vt_int = random.choice(Competidor.listaCompetidor)
        Competidor.listaCompetidor.remove(self.vt_int)
        votos_internet = [1000, 2000, 3000, 4000, 5000]
        votos_telefone = [1000, 2000, 3000, 4000, 5000]
        self.indicado1 = random.choice(votos_internet) + random.choice(votos_telefone)
        self.indicado2 = random.choice(votos_internet) + random.choice(votos_telefone)
        if self.indicado1 < self.indicado2:
            self.eliminado = self.paredao_1
        if self.indicado2 < self.indicado1:
            self.eliminado = self.vt_int
        print "\n", Provas.objetivo, "\n"
        print "Este é o Líder da Semana\n", self.lider, "\n"
        print "Esté o Anjo da Semana\n", self.anjo, "\n"
        print "Este é o Imunizado da Semana\n", self.imunizado, "\n"
        print "Este é o Sujeito do Paredão da Semana\n", self.paredao_1, "\n"
        print "Este é o Sujeito Indicado 2 por Votacao Interna\n", self.vt_int, "\n"
        print "Este é o Sujeito Eliminado pelo Paredao\n", self.eliminado, "\n"
        return self.lider, self.anjo, self.imunizado, self.paredao_1, self.vt_int, self.eliminado
       
class Paredao(object):
    prova1 = Provas("Realizacao do Paredao", "Pedro Bial", "Eliminar um Sujeito", "!!!!")
    prov1 = prova1.defineLider_Anjo_Imunizado_Paredao1_VotInterna()

         
class Produto:
    leite = 50
    margarina = 100
    pao = 10
    queijo = 100
 
class Compra:
    
    Pagar = []
    Qtd_Compra = []
    for i in range(Edicao.week):
        qtd_Leite = int(input("Digite Quantidade Leite: "))
        qtd_Margarina = int(input("Digite Quantidade Margarina: "))
        qtd_Pao = int(input("Digite Quantidade Pao: "))
        qtd_Queijo = int(input("Digite Quantidade Queijo: "))  
        Qtd_Compra = (qtd_Leite + qtd_Margarina + qtd_Pao + qtd_Queijo)
        Pagar = (qtd_Leite*Produto.leite) + (qtd_Margarina*Produto.margarina) + (qtd_Pao*Produto.pao) + (qtd_Queijo*Produto.queijo)
        dataCompra = date.randomDate("05-01-2014", "19-01-2014", random.random())
        print Pagar, "Pagou esse valor pela Compra desse Dia\n"
        print Qtd_Compra, "Quantidade Total da Compra\n"
        print dataCompra , "Compra Realizada Nesta Data!"
        print qtd_Leite, "Numero de Leites\n"
        print qtd_Margarina, "Numero de Margarinas\n"
        print qtd_Pao, "Numero de Pãos\n"
        print qtd_Queijo, "Numero de Queijos\n"
 
class Prato:
    quem_fez_cafe = ""
    dataPrato = ""
    for i in range(Edicao.week):
        quem_fez_cafe = random.choice(Competidor.listaCompetidor)
        print quem_fez_cafe , "Esse Participante fez o café!\n"
        dataPrato = date.randomDate("05-01-2014", "19-01-2014", random.random())
        print date.randomDate("05-01-2014", "19-01-2014", random.random())

