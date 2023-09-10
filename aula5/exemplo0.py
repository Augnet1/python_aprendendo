"""
Formatando valores com modificadores - Aula 5

:s - Texto (strings)
:d - Inteiros (int)
:f - Número de pontos flutuantes (float)
:.(NUMERO)f - Quantidade de casas decimais (float)
:(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO - s, d ou f)

> - Esquerda
< - Direita
^ - Centro
"""
num_1 = 10
num_2 = 3
divisao = num_1 / num_2

# Valor sem formatação
print('Valor sem formatação: ', divisao)
print()

# : indica o início do modificador, .2 duas casas decimais depois do ponto e f de float
print('Modificador -> :.2f')
print(': Indica o início do modificador')
print('.2 Indica a quantidade de casas decimais(2, no caso) depois do ponto')
print('f Tipo float')
print('----------')
print('Valor formatado com a função format(), sem modificador: {}'.format(divisao))
print(
    'Valor formatado com a função format(), com modificador: {:.2f}'.format(divisao))

print(f'Valor formatado com f strings, sem modificador: {divisao}')
print(f'Valor formatado com f strings, com modificador:: {divisao:.2f}')

print('----------')

nome = 'Luiz Gonzaga'
print(f'O nome é {nome:s}')

print('----------')
num_1 = 2
num_2 = 1150

# Completa o num_1 e num_2 com zeros à esquerda até completar 10 dígitos
print(f'{num_1:0>10}')
print(f'{num_2:0>10}')
print(num_1)
print(num_2)

print()

# Completa o num_1 e num_2 com zeros à direita até completar 10 dígitos
print(f'{num_1:0<10}')
print(f'{num_2:0<10}')
print(num_1)
print(num_2)

print()

# Completa o num_1 e num_2 com zeros à direita e esquerda, deixando o número no centro até 10 dígitos
print(f'{num_1:0^10}')
print(f'{num_2:0^10}')
print(num_1)
print(num_2)

print()

# Completa o num_1 e num_2 com duas casas decimais, simulando um float
print(f'{num_1:.2f}')
print(f'{num_2:.2f}')
print(num_1)
print(num_2)

print()

# Completa o num_1 e num_2 com duas casas decimais, simulando um float e com zeros à esquerda até completar 10 dígitos
print(f'{num_1:0>10.2f}')
print(f'{num_2:0>10.2f}')
print(num_1)
print(num_2)

print()
nome = 'Luiz Gonzaga'

# Completa a string nome com # à direita e à esquerda até completar 50 dígitos
print(f'{nome:#^50}')

# Ajusta o nome à esquerda, adicionando # até 20 dígitos
print(nome.ljust(20, "#"))
print(nome.lower())  # Tudo minúscula
print(nome.upper())  # Tudo maiúscula
print(nome.title())  # Primeiras letras maiúsculas

print('----------')
print()
