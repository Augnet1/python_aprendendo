"""
for
Iterando string com for
Função range(start=0, stop, step=1)
"""
texto = 'Python'

for letra in texto:
    print(letra)
print()
print('----------')

for n, letra in enumerate(texto):
    print(n, '-> ', letra)
print()
print('----------')

for numero in range(10):  # padrão range start=0 step=1
    print(numero)
print()
print('----------')

for numero in range(2, 20, 2):
    print(numero)
print()
print('----------')

for numero in range(20, 10, -1):  # Não imprime o valor do stop
    print(numero)
print()
print('----------')

texto = 'Python'
nova_string = ''

# continue - pula para o próximo laço
# break - termina o laço
for letra in texto:
    if letra == 't':
        continue  # Não vai colocar a letra 't'
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
        break  # Depois de colocar a letra 'h' em maiúscula acaba o laço
    else:
        nova_string += letra
print(nova_string)
