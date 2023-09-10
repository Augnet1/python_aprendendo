"""
while em Pyton - Aula 7

utilizado para realizar ações enquanto
uma condição for verdadeira.

Requisitos: Entender condições e operadores
"""
# Repetir 5 vezes
# print('Linha 1')
# print('Linha 1')
# print('Linha 1')
# print('Linha 1')
# print('Linha 1')
# print('Acabou!')
print('----------')
x = 0
# Com while
while x <= 10:
    if x % 2 == 0:
        x += 1
        continue
    print('Linha', x)
    x += 1
print('----------')
x = 0  # Coluna
while x < 10:
    y = 0  # Linha
    while y < 5:
        print(f'(Coluna,Linha)->({x+1},{y+1})')
        y += 1
    x += 1
print('----------')
while True:
    print()
    num_1 = input('Digite um número: ')
    num_2 = input('Digite outro número: ')
    operador = input('Digite um operador:')

    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Você precisa digitar um número válido!')

    num_1 = int(num_1)
    num_2 = int(num_2)

    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '*':
        print(num_1 * num_2)
    elif operador == '/':
        print(num_1 / num_2)
    else:
        print('Operador inválido!')

    sair = input('Deseja sair? [s]im ou [n]ão')
    if sair == 's':
        break
