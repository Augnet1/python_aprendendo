"""
Listas
Fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""
# Suporta vários valores de tipos diferentes
#         0    1    2    3    4
lista = ['A', 'B', 'C', 'D', 'E']
#        -5   -4   -3   -2   -1
string = 'ABCDE'

listaDiversa = ['A', 2, 'C', 41.5, 40, 10.5]
listaDiversa[4] = 'Qualquer outra coisa'
print(lista)
print()
print(lista[3])
print()
print(lista[-4])
print()
print(listaDiversa)
print()
print(listaDiversa[4])
print()
print(listaDiversa[0:3])  # De 0 à 3 (3 não incluso)
print()
print(listaDiversa[1:2])  # De 0 à 2 (3 não incluso)
print()
print('Lista: ', listaDiversa)  # Inverte a lista
print('Inverte a lista: ', listaDiversa[::-1])  # Inverte a lista
print()
print('Lista: ', listaDiversa[::2])  # Começa no 0 até o fim pulando de 2 em 2
print('----------')
l1 = [1, 2, 3]
print('l1: ', l1)
l2 = [4, 5, 6]
print('l2: ', l2)
l3 = l1 + l2
print('l3: ', l3)
print()
l1.extend(l2)  # Junta valor à lista
print('l1: ', l1)
l1.extend('a')  # Junta valor à lista
print('l1: ', l1)

# append -> insere um valor no final da lista
l2.append(l1)  # Adiciona 1 valor
print('l2: ', l2)
print('----------')

# insert -> Insere um valor no índice indicado,
# recalculando os demais índices necessários
l2.insert(0, 'banana')
print('l2: ', l2)
print('l2[0]: ', l2[0])
print('----------')

# pop -> apagar o último valor da lista
print('l2 (antes do pop): ', l2)
l2.pop()
print('l2 (depois do pop): ', l2)
print('----------')

#     0  1  2  3  4  5  6  7  8
l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print('l2: ', l2)
del(l2[0])  # Apaga a posição 0
print('l2: ', l2)
del(l2[1:4])  # Apaga as posiçõe 1, 2, 3 (4 não está incluso)
print('l2: ', l2)

print('----------')

print('l2: ', l2)
print('Máxima de l2: ', max(l2))
print('Mínima de l2: ', min(l2))

print('----------')
l2 = list(range(1, 10))
print('l2: ', l2)
print('----------')

secreto = 'perfume'
digitadas = []
chances = 3

while True:
    if chances <= 0:
        print('Você perdeu!!!')
        break
    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Ahhh, isso não vale, digite apenas uma letras.')
        continue
    if letra in digitadas:
        print(f'A letra "{letra}" já foi digitada.')
        print()
    else:
        digitadas.append(letra)
        if letra in secreto:
            print(f'UHUULLL, a letra "{letra}" existe na palavra secreta.')
            print()
        else:
            print(f'AFFFzzz, a letra "{letra}" NÃO EXISTE na palavra secreta.')
            print()
            digitadas.pop()

        secreto_temporario = ''
        for letra_secreta in secreto:
            if letra_secreta in digitadas:
                secreto_temporario += letra_secreta
            else:
                secreto_temporario += '*'

        if secreto_temporario == secreto:
            print('----------')
            print(
                f'Que legal, VOCÊ GANHOU!!! A palavra era {secreto_temporario}.')
            print('----------')
            break
        else:
            print(f'A palavra secreta está assim: {secreto_temporario}')
            print()
        print(digitadas)
    if letra not in secreto:
        chances -= 1
    print(f'Você ainda tem {chances} chances.')
    print()
