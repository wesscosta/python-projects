import math


x = int(input('Digita um numero: '))
b = y = int(input('Digita um numero: '))


print(math.exp(x)) #Retorna e elevado a X
print(math.log2(x)) #Retorna o logaritimo de x na base 10
print(math.log10(x)) 
print(math.log(x,b)) #Retorna o logaritimo de x na base b ( de acordo com a documentação do Python, deve ser utilizado apenas quando b é diferente de 2 e 10)
print(math.pow(x,y)) #Retorna x elevado a y;