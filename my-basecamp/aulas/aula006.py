#### Tipos Primitivos #####
# int   - Numeros Inteiros
# float - Numeros Rais 
# bool  - Logicos ou Boleano (True or False) iniciais com letra maiuscula 
# str   - String, texto


# n1 = int(input('Digite um numero: '))
# n2 = int(input('Digite mais um numero: '))
# s=n1+n2

# print('A soma entre {} e {} vale {}'.format(n1, n2, s))


teste = input( 'Digite um número: ')
print (type(teste))

print(type(int(teste)))
print(type(float(teste)))
print(type(bool(teste)))
print(type(str(teste)))
print('')
print('É numero? {}' .format(teste.isalnum()))
print('É letra? {}' .format(teste.isalpha()))


