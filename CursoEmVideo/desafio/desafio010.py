# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
# Considere US$ 1.00 = R$3,27

saldoEmReal = float(input('Digite o saldo que você tem na carteira em Real: '))
cotacao = 3.27


saldoEmDolar = saldoEmReal / cotacao

print('Com esse saldo de R$ {:.2f}, você pode compra US$ {:.2f}! \n' .format(saldoEmReal, saldoEmDolar))
