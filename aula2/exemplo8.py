'''
Introdução aos tipos de dados

int - número inteiros (positivos, begativos e zero)
float - números reais, com ponto (positivos ou negativos)
bool - valor lógico (booleano) - True = verdadeiro, False = falso
str - String ou cadeia de caracters (texto)
... Existem mais tipos de dados

Tudo no python é um objeto, incluindo os tipos primitivos

Só é possível usar operador de + com valores de mesmo tipo
Para cocatenar valores diferentes, é necessário
fazer um cast (conversão) dos valores
É possível realizar operações aritméticas entre int e float
'''

inteiro = 5 # int
real = 6.2 # float
booleano = True # bool
texto = '9.3' # str
texto2 = 'Texto'

print('Variável inteiro: ', inteiro, ' - Tipo: ', type(inteiro))
print('Variável real: ', real, ' - Tipo: ', type(real))
print('Variável booleano: ', booleano, ' - Tipo: ', type(booleano))
print('Variável texto: ', texto, ' - Tipo: ', type(texto))
print('-----------')

print('Variável inteiro + real: ', inteiro + real) # 5 + 6.2 = 11.2

# print(inteiro + texto) # erro

print('Variável inteiro + float(texto): ', inteiro + float(texto)) # 5 + 9.3 = 14.3
print('-----------')

print('Tipo da variável texto: ', type(texto)) # str - Tipo da variável texto

# Cast (convertendo a variável "texto" - string em float)
texto_float = float(texto)
print('Variável texto_float recebe o cast float(texto)')
print('Variável e tipo da variável texto_float: ', texto_float, type(texto_float)) # float - Tipo da variável texto_float
print('Variável inteiro + texto_float: ', inteiro + texto_float) # 5 + 9.3 = 14.3
print('-----------')

# Cast (convertendo a variável "texto" - string em float, depois em int)
texto_int = int(float(texto))
print('Variável texto_int recebe o cast int(float(texto))')
print('Variável e tipo da variável texto_int: ', texto_int, type(texto_int)) # int - Tipo da variável texto_int
print('Variável inteiro + texto_int: ', inteiro + texto_int) # 5 + 9 = 14
print('-----------')

# Cast (tentando converter texto2 em int)
# Não é possível converter texto em int, só se a string for só um número, mas texto não
# print(int(texto2)) # erro
print('Variável inteiro: ', inteiro)
print('O tipo da variável inteiro é: ', type(inteiro)) # int
inteiro = str(inteiro) #str
print('O tipo da variável inteiro é: ', type(inteiro)) # str
print('-----------')

# Valores lógicos (bool), geralmente são usados em comparações
variavel = 10>2
print('10 > 2', variavel)
print()
variavel2 = 10<2
print('10 < 2', variavel2)


