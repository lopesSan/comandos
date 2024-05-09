#Metodo abordado: from random, import choise#
"""Esse execício simula uma escolha automática de nomes ou objetos em uma determinada lista fornecida ao Python"""
from random import choice
n1 = str(input('Digite o nome do primeiro aluno: \n'))
n2 = str(input('Digite o nome do segundo aluno: \n'))
n3 = str(input('Digete o nome do terceiro aluno: \n'))
n4 = str(input('Digite o nome do quarto aluno: \n'))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('O aluno selecionado para a próxima fase será: {}'.format(escolhido))

#Metodo abordado: import random#
import random
n1 = str(input('Digite o nome do primeiro aluno: \n'))
n2 = str(input('Digite o nome do segundo aluno: \n'))
n3 = str(input('Digite o nome do terceiro aluno: \n'))
n4 = str(input('Digite o nome do quarto aluno: \n'))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O aluno selecionado para a próxima fase será: {}'.format(escolhido))

