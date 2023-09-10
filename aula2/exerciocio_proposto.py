'''
Crie 5 variáveis referente aos dados de uma pessoa
Variáveis: nome, sobrenome, idade, altura e peso.

Exiba uma apresentação da pessoa, da seguinte forma:

Este é o(a) #nome #sobrenome. Ele/Ela nasceu em #ano_nascimento e tem
#idade anos. #nome #sobrenome tem #altura de altura e pesa #peso kilos.
'''

nome = 'Luiz Gonzaga'
sobrenome = "Silva"
idade = 28
altura = 1.85
peso = 85

ano_nascimento = 2022 - idade

print(f'Este é o(a) {nome} {sobrenome}. Ele/Ela nasceu em {ano_nascimento} '
    f'e tem {idade} anos. {nome} {sobrenome} tem {altura} de altura e pesa '
    f'{peso} kilos.')