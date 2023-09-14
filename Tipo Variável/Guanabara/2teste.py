n = float(input('Digite um valor:'))
print(n)
# Resltado: Digite um valor: 4
# 4.0

# OUTRO 

n = str(input('Digite um valor:'))
print(n)
# Resultado 6 
# Mas se colocar em outro jeito 
print(type(n))
# Resultado: Digite valor: 6 
# <class 'str'>
n = input('Digite um valor: ')
print(type(n))
# Resultado: Digite um valor: 88
# <class 'str'> 

# OUTRO 

n = bool(input('Digite um valor:'))
print(type(n))
# Resultado: Digite um valor: 7 
# <class 'bool'> 
# mas se colocar outro 
print(n)
# Resultado: O BOLEANO SÓ MOSTRA VERDADEIRO OU FALSO / TRUE OR FALSE
# Digite um valor: 4 
# True 
print(n)
# Dentro do resultado se vc não colocar um valor ele fica falso 
# Resultado: False
# Pq não tem nenhum número 
 
# True
n = input('Digite algo')
print(n.isnumeric())
# numeric / só tem que ser numero
# Resultado: Digite algo: 3 
# True 

# False
# Resultado: Digite algo: oi
# False 

# False
# Resultado: Digite algo: 3a
# False

# OUTRO
n = input('Digite algo')
print(n.isalpha())
# alpha de alfabetico / ou seja tem que ser só letras
# Resultado: www 
# True 

# Resultado: 123
# False

# Resultado: 3a 
# False

# OUTRO
n = input('Digite algo')
print(n.isalnum())
# Ele é alfabetico e númerico / serve para os dois
# Resultado: Digite algo: oi
# True

# Resultado: 3a
# True

# Resutado: 7
# True 

# Resultado: 
# False

# OBS: Tem varios IS / pode ser letras grandes, pequenas, númeors...






