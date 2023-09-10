'''
Aula 2
- Comentários
- A função print (mais um modo de uso)
- Alguns detalhes da linguagem python (básico)
- Operadores Aritméticos
- Variáveis
- Introdução aos tipos de dados (str, int, float e bool)

    3 aspas (simples ou duplas) são usadaas para gerar
    textos (string) com quebra de linha ou documentação

    (isso NÃO é um comentário)
'''

# Isso é um comentário
print(123456) # Isso também é um comentário

# print(789)

# Imprime linhas 1 2 4 e 5
print('Linha 1')
print('Linha 2')
# print('Linha 3')
print('Linha 4') # fiz isso por isso
print('Linha 5')

# 3 aspas (simples ou duplas) não é comentário, a prova disso é que se declararmos um variável
# com o conteúdo citado e dermos um print, o print imprime todo o conteúdo. Exemplo abaixo.
# Mas pode ser utilizado como comentário e não usar seu conteúdo em uma variável.

var = """
# Imprime linhas 1 2 4 e 5
print('Linha 1')
print('Linha 2')
# print('Linha 3')
print('Linha 4') # fiz isso por isso
print('Linha 5')
"""
print(var)