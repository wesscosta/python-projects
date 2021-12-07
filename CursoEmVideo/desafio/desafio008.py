# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.
#### Desafio 008 ####

metro = float(input('Digite um valor em metros: '))

print('{:.2f} metros equivale a {:.2f} centimentros e {:.2f} milimetros'.format(metro, metro*100, metro*1000))