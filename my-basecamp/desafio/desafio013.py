# Faça um algoritmo que  leia o salario de um funcionario e mostre seu novo salario com 15% de aumento
#### Desafio 013 ####

salario = float(input('Digite seu salario: '))
novoSalario =salario + (salario * 15/100)

print('O atual salario é {} e apois aumento de 15% ficara {:.2f}.'.format(salario,novoSalario))