"""
Manipulando strings - Aula 6

- String indices
- Fatiamento de strings
- Funções buit-in len, abs, type, print, etc...
Essas funções podem ser usadas diretamente em cada tipo.

Você pode conferir tudo isso em:
https://docs.python.org/3/library/stdtypes.html (tipos built-in)
https://docs.python.org/3/library/functions.html (funções built-in)
"""
# positivos [012345678]
texto = "Python s2"
# negativos -[987654321]
print(texto[0])
print(texto[1])
print(texto[2])
print(texto[3])
print(texto[4])
print(texto[5])
print(texto[6])
print(texto[7])
print(texto[8])
print()
print('Tamnaho: ', len(texto))
print()
print(texto[-9])
print(texto[-8])
print(texto[-7])
print(texto[-6])
print(texto[-5])
print(texto[-4])
print(texto[-3])
print(texto[-2])
print(texto[-1])

url = 'www.google.com.br/'

print(url[:-1])

nova_string = texto[2:6]

print(nova_string)
