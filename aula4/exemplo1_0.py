"""
Condições IF, ELIF e ELSE - Aula 4
"""
print('IF: True')
if True:
    print('Verdadeiro.')

    num_1 = 2
    num_2 = 4

    print(num_1 + num_2)
print('Fora do if.')

print()
print('IF: False ELSE:')
if False:
    print('Verdadeiro.')
else:
    print('Falso.')

print()
if False:
    print('Verdadeiro.')
elif True:
    print('Agora é verdadeiro.')
else:
    print('Não é verdadeiro.')
