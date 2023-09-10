"""
Iterando strings com while
"""
minha_string = 'O rato roeu a roupa do rei de roma.'

# string é imutável, por isso não dá para mudar elementos separados
# minha_string[2] = 'R'

print(minha_string[2])

tamanho_string = len(minha_string)

c = 0

nova_string = ''
while c < tamanho_string:

    if minha_string[c] == 'r':
        nova_string = nova_string + minha_string[c].upper()
    else:
        nova_string = nova_string + minha_string[c]
    print(f'Contador: {c} -> ', nova_string)

    c += 1
print()
print('String original \'minha_string\':', minha_string)
print('Nova string \'nova_string\':', nova_string)
print('Quantas letras \'a\' tem em \'minha_string\':', minha_string.count('a'))
print('----------')
while True:
    frase = input('Digite uma frase: ')
    c = 0
    contagem_atual = 0
    letra = ''
    while c < len(frase):
        qtd_vezes_letras = frase.count(frase[c])

        # minha_string[c].strip() retira espaço
        if contagem_atual < qtd_vezes_letras and frase[c].strip():
            letra = frase[c]
            contagem_atual = qtd_vezes_letras

        c += 1
    print(letra, contagem_atual)
print()
