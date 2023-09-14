# Tipos primitivos

n1=input("Digite um número:")
# OBS: DENTRO DO PYTHON PODE USAR DOIS TIPOS DE ASPAS ' E "" MAS A COMUNIDADE PREFERE USAR '

# n1 tem o resultado de 1 input, como se fosse recebe

n2=input('Digite mais um número:')
# Nesse caso iremos ler dois valores 
# Agora iremos somar esses dois valores na qual iremos colocar dentro de outra variavel

s=n1+n2

# Agora colocamos o print que é o comando para escrever na tela 
print("A soma vale",s)

# OBS: Ao abrir um espaço n1=  input('') quando se da um input o valor que é digitado dentro do input, mesmo que 
#seja um numero ele é considerado uma STRING

# OUTRO TIPO PRIMITIVO 

n1=int(input('Digite um numero:'))
# OBS: Dentro do espaço laranja vai ser convertido para números inteiros 
n2=int(input('Digite mais um número:'))

# OBS NÚMEROS INTEIROS É = 3,4,5 UMA SÉRIE DE NÚMEROS

# TIPOS PRIMITIVOS MAIS BASICOS SÃO : 
# int
# float
# bool
# str

int # é um número inteiro = 7 -4 0 e 9875 tbm é número inteiro / número positivo e negativo o que for é inteiro 

float # 4.5 0.076 o que eles tem em comum é o ponto flutuante / números reais -15.223 
#/ 7.0 é inteiro mas o que muda do outro é que ele é real 

bool # O valor BOLEANO só aceita dois valores / o valor verdadeiro TRUE T sempre usar o T maiusculo 
#/ e o valor FALSE 

str # Seria um "OLÁ" e todas as palavras tem que estarem entre "" / e tbm '7.5' é uma string 
#/ '' STRING vazia tbm pode 

# OUTRA MANEIRA DE USAR O PRINT

print('A soma vale',s)

# PRINT semelhante mas com mais recurso 

print('A soma vale()'.format(s)) 

# Dentro desses () iramos colocar o S para substituir a mascara verde -> ()


