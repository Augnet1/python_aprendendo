"""
Operadores relacionais - Aula 4
==  igualdade
>   maior que
>=  maior que ou igual a
<   menor que
<=  menor que ou igual a
!=  diferente
"""
print('2 == 2')
print(2 == 2)  # True

print()
print('num_1 = 2')
num_1 = 2  # int
print(num_1)  # int
print()
print('num_2 = \'2\'')
num_2 = '2'  # str
print(num_2)  # str

print()
print('2 == \'2\'')
print(num_1 == num_2)  # False

print('----------')
print()

num_1 = 2
num_2 = 2

# expressao = num_1 == num_2
# operador = '=='

# expressao = num_1 > num_2
# operador = '>'

# expressao = num_1 >= num_2
# operador = '>='

# expressao = num_1 < num_2
# operador = '<'

# expressao = num_1 <= num_2
# operador = '<='

expressao = num_1 != num_2
operador = '!='

print('num_1(', num_1, ') ', operador, ' num_2(', num_2, ')')
print(expressao)

print()
print('----------')
print()

nome = input('Qual o seu nome? ')
idade = input('Qual a sua idade? ')
print('Empréstimos para maiores de 18 anos.')
print()
idade = int(idade)
idade_limite = 18
idade_menor = 20  # Muito jovem
idade_maior = 30  # Passou da idade

if idade >= idade_limite:
    print(f'{nome} pode pegar o empréstimo.')
else:
    print(f'{nome} NÃO pode pegar o empréstimo.')
print()
print('----------')
print('Empréstimos entre 20 e 30 anos.')
print()
if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome} pode pegar o empréstimo.')
else:
    print(f'{nome} NÃO pode pegar o empréstimo.')
