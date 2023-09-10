'''
Variáveis

Variáveis são utiliza para armazenar valores e dar
nome a um trecho de memória do computador onde
os valores estão armazenado.

Quando uma variável é criada, o python já determina
qual o seu tipo baseando-se no seu valor (Tipagem dinâmica).

Nomes de variáveis devem iniciar com uma letra.
Nomes de variáveis podem conter números.
Nomes compostos pode ser separdos por um _
Por convenção, utilize apenas letras minúsculas.
'''

nome = 'Luiz Gonzaga' # string
idade = 25 # int
altura = 1.80 # float
peso = 100 # int
data_atual = '25/11/2022' # string

# Fórmula IMC = peso dividido pelo quadrado da altura
indice_massa_corporal = peso / (altura ** 2)
indice_massa_corporal = '{:.2f}'.format(indice_massa_corporal)

print('A variável nome recebeu: ', nome)
print('A variável idade recebeu: ', idade)
print('A variável altura recebeu: ', altura)
print('A variável peso recebeu: ', peso)
print('A variável data_atual recebeu: ', data_atual)

# Uma forma de mostrar
print()
print(nome, 'tem', idade, 'anos e seu IMC é', indice_massa_corporal)

# Outra forma de mostrar: utilizando a função format
print()
print('{} tem {} anos e seu IMC é {}.'.format(nome, idade, indice_massa_corporal))

# Mais uma forma de mostrar: utilizando a função format
print()
print(f'{nome} tem {idade} anos e seu IMC é {indice_massa_corporal}.')

# Mais uma forma de mostrar: utilizando a função format
print()
print('{0} tem {1} anos e seu IMC é {2}.'.format(nome, idade, indice_massa_corporal))

# Mais uma forma de mostrar: utilizando a função format
print()
print('{n} tem {i} anos e seu IMC é {im}.'.format(n=nome, i=idade, im=indice_massa_corporal))

# Outra forma de usar variável
mensagem = f'''
Um texto
gigante
aqui
e agora eu vou
exibir as minhas variáveis.
Variável nome: {nome}
Variável idade: {idade}
Variável altura: {altura}
Variável peso: {peso}
Variável índice de massa corporal: {indice_massa_corporal}
'''
print(mensagem)