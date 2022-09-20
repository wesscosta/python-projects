# Crie um algoritimo que leia um numero e mostre o seu dobro, triplo e raiz quadrada.
#### Desafio 06 ####

num = int(input('Digite um número: '))

dobro = num * 2
triplo = num * 3
rq = num ** (1/2)
print(' O dobro é: {} \n o triplo é: {} \n e a Raiz Quadrada é: {:.3}'.format(dobro,triplo, rq))