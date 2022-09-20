# Faça um programa que leia algo pela tela e mostre na tela  o seu tipo primitivo e todas as informações posiveis sobre ela.
#### Desafio 004 ####

a = input('Digite a: ')
print('')
print('O que você digitou é do tipo {}.'.format(type(a)))
print('a.isalnum(): {}' .format(a.isalnum())) # Alfanumerica
print('a.isalpha(): {}' .format(a.isalpha())) # Letra
print('a.isascii(): {}' .format(a.isascii())) 
print('a.isdecimal(): {}' .format(a.isdecimal()))
print('a.isdigit(): {}' .format(a.isdigit())) 
print('a.isidentifier(): {}' .format(a.isidentifier()))
print('a.isnumeric(): {}' .format(a.isnumeric()))
print('a.isprintable(): {}' .format(a.isprintable()))
print('a.isspace(): {}' .format(a.isspace()))
print('a.isalpha(): {}' .format(a.istitle())) 
print('a.isupper(): {}' .format(a.isupper())) # Maiusculo
print('a.islower(): {}' .format(a.islower())) # minusculo
print('a.istitle(): {}' .format(a.istitle))) # Nem maiusculo nem minuscula