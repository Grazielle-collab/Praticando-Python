n1 = input('Digite um valor:')
print(type(n1))
# OBS: O resutado do valor tem que dar 5 
# A class dela saiu 'str'>

n1 = int(input('Digite um valor:'))
print(type(n1))
# OBS: O resultado do valor foi 5 
# Mas a class foi 'int' um valor inteiro 

n1 = int(input('Digite um valor'))
n2 = int(input('Digite outro:'))
s = n1 + n2 
print('A soma vale', s)
# OBS: Nesse caso quero que o S receba n1 + n2
# No print quero que escreva a soma vale S 
# Resultado: Digite um valor: 5
# Digite outro valor:3
# A soma vale 8 

# TIRANDO O INT

n1 = (input('Ditite um valor'))
n2 = (input('Digite outro:'))
s = n1 + n2 
print('A soma vale', s)
# OBS: Nesse caso ele não some e por isso deu esse resultado 
# Resltado: Digite um valor: 5 
# Digite outro valor: 3
# A soma vale 53

# COMO FAZER 6 E 2 VALER = 8 

n1 = int(input('Digite um valor:'))
n2 = int(input('Digite outro:'))
s = n1 + n2 
print('A soma entre', n1, 'e', n2, 'vale', s)
# Resultado: Digite um valor: 6 
# Digite outro: 2
# A soma entre 6 e 2 vale 8

# Agora mudando o PRINT
print('A soma entre {} e {} vale {}'.format(n1,n2,s))
# print('A soma entre {0} e {1} vale {2}'.format(n1,n2,s))
# Diz ser mais facil 

# Resultado; Digite um valor: 5
# Digite outro: 9
# A soma entre 5 e 9 vale 14 


