#coding: utf-8

from Exercicio_Python import Apresentacao
import random

class ProvaDinheiro(object):
    ProvaDinheiro = []
    Lista_Valores = [1500, 2000, 3000, 4000, 5000]
    for i in range(Apresentacao.n):
        NProvaDinheiro = random.choice(Lista_Valores)
    print NProvaDinheiro