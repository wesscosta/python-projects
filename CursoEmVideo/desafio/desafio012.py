# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço. com 5% de desconto.
#### Desafio 012 ####

valor = float(input('Digite o valor do produto: '))
desconto = 5 / 100
valorDesconto = valor * desconto 
print('O novo valor deste produto com {:.0f}% de desconto é R${:.2f}.' .format(desconto*100, valor - valorDesconto))