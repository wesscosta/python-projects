# Faça um programa que leia a largura e a altura de uma parede em metros, cálcule a sua área e a quantidade de tinta necessaria para pintá-la, sabendo que cada litro de tinta pinta uma ára de 2m²
#### Desafio 011 ####

altura = float(input('Digite a altura em metros: '))
largura = float(input('Digite a largura em metros: '))

metros2 = altura * largura

print('Para pinta esse area de {}m², você ira utilizar {}L de tinta.'.format(metros2, metros2/2))