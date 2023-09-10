'''
Operadores aritméticos
Os operadores aritméticos no python são:

+   sinal de mais               Adição/Cocatenação
-   sinal de menos              Subtração
*   asterisco                   Multiplicação/Repetição
/   barra                       Divisão
//  duas barras                 Divisão com resultado inteiro
%   sinal de porcentagem        Módulo (resto da divisão)
**  dois asteriscos             Exponenciação

As operações de mesma prioridade são realizadas da esquerda para direita
Os parenteses () alteram a prioridade

'''
print('Operador +:')
print('Soma 2 com 2: ', 2 + 2) # 4
print('Concatena 2 com 2: ', '2' + '2') # 22
print()
print('Operador *:')
print('Multiplca 3 com 3: ', 3 * 3) # 9
print('Repete "A" 5 vezes: ', 'A' * 5) # AAAAA
print()
print('Operador /:')
print('Divide 10 com 3: ', 10 / 3) # 3.3333333333333335
print()
print('Operador //:')
print('Divide 10 com 3 (valor inteiro): ', 10 // 3) # 3
print()
print('Operador %:')
print('Resto da divisão entre 10 e 3: ', 10 % 3) # 1
print()
print('Operador **:')
print('2 elevado a 3: ', 2 ** 3) # 8
print()
print('Alterando a prioridade com ():')
print('5+2*10 é: ', 5+2*10) # 25
print('(5+2)*10 é: ', (5+2)*10) # 70
