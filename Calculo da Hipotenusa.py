#Primeira possibilidade#
"""Calculando o valor da hipotenusa"
co = float(input('Digite o valor do comprimento do cateto oposto \nCO= '))
ca = float(input('Digite o valor do comprimento do cateto adjacente \nCA= '))
hi = (co**2 + ca**2) **(1/2)
print('O valor total da hipotenusa é de {:.2f}'.format(hi))"""

#Segunda possibilidade#
"""import math
co = float(input('Digite o valor do comprimento do cateto oposto \nCO= '))
ca = float(input('Digite o valor do comprimento do cateto adjacente \nCA= '))
hi = math.hypot(co, ca)
print('O valor total da hipotenusa é de {:.2f}'.format(hi))"""

#Terceira possibilidade#
"""from math import hypot
co = float(input('Digite o comprimento do cateto oposto \nCO= '))
ca = float(input('Digite o comprimento do cateto adjacente \nCA= '))
hi = hypot(co, ca)
print('O valor total da hipotenusa é de {:.2f}'.format(hi))"""
