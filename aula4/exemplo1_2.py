"""
Operadores lógicos - Aula 4
and     e
or      ou
not     inversão
in      Está incluso
not in  Não está incluso
"""
a = 2
b = 2
c = 3

print('Operador: and')
# and
# (True and True) = True
# (False and True) = False
# (True and False) = False
# (False and False) = False

print('a =', a, ', b =', b, ', c =', c)
print('(a == b) and (b < c) => True and True => ', a == b and b < c)  # True
print('(a != b) and (b < c) => False and True => ', a != b and b < c)  # False
print('(a == b) and (b > c) => True and False => ', a == b and b > c)  # False
print('(a != b) and (b > c) => False and False => ', a != b and b > c)  # False
print('----------')

print('Operador: or')
# or
# (True or True) = True
# (False or True) = True
# (True or False) = True
# (False or False) = False

print('a =', a, ', b =', b, ', c =', c)
print('(a == b) or (b < c) => True or True => ', a == b or b < c)  # True
print('(a != b) or (b < c) => False or True => ', a != b or b < c)  # True
print('(a == b) or (b > c) => True or False => ', a == b or b > c)  # True
print('(a != b) or (b > c) => False or False => ', a != b or b > c)  # False
print('----------')

print('Operador: not')
# not
# not True = False
# not False = True
print('not True =>', not True)  # False
print('not False =>', not False)  # True
print()

a = ''  # Equivalente a False, pois não tem string "sem um valor"
b = 0   # Equivalente a False, pois é um int 0 "sem um valor"

print('A é: ', a, '- Tipo de A: ', type(a))
print('B é: ', b, '- Tipo de B: ', type(b))
if not a:
    print('Por favor informar o valor de A.')
if not b:
    print('Por favor informar o valor de B.')
print()
a = 'Texto qualquer'
b = 1
print('A é: ', a, '- Tipo de A: ', type(a))
print('B é: ', b, '- Tipo de B: ', type(b))
if not a:
    print('Por favor informar o valor de A.')
if not b:
    print('Por favor informar o valor de B.')
print('----------')

print('Operador: in')

nome = 'Luiz Gonzaga'
print(f'Nome: {nome}')
print()

palavra = input('Procurar: ')
if palavra in nome:
    print(f'Existe {palavra} no nome {nome}.')
else:
    print(f'NÃO existe {palavra} no nome {nome}.')

print()

if 'n' in nome:
    print('Existe a letra N no seu nome.')

if 'k' not in nome:
    print('NÃO existe a letra K no seu nome.')
print('---------')
print()

usuario = input('Nome do usuário: ')
senha = input('Senha do usuário: ')

usuario_bd = 'admin'
senha_bd = '123456'

if usuario_bd == usuario and senha_bd == senha:
    print('Você está logado no sistema')
else:
    print('Usuário ou senha inválidos.')
