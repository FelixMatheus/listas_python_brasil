#coding: utf-8

f=open("palavras.txt","r")
lista = f.readlines()
f.close()

palavra = []

for i in lista:
    palavra.append(i)

print palavra

#Existem 8 palavras, escolha 1 -> digite um número de 1 a 8
n = input("Digite um número: ")
palavra_escolhida = palavra[n-1]
print palavra_escolhida

#Você tem 6 tentativas:

letra = raw_input("Digite uma letra: ")
i = 0
nova_palavra = ""
while i<6:
    if not letra in palavra_escolhida:
        i = i + 1
        print "Você errou, tente outra vez"
        letra = raw_input("Digite outra letra: ")
    
    if letra in palavra_escolhida:
        letra = raw_input("Digite outra letra: ")
        i = i
        nova_palavra += nova_palavra
        print nova_palavra
        print "Parabens você acertou! "
    
        
    
    