'''Escreva um programa que uma sequência de nomes e mostre-os em ordem alfabética. 
O programa deve parar de ler quando o usuário digitar fim.'''

control = 0
words = 0
words_list = []
while words != 'fim':
    words = str(input('Enter a word: '))
    if words == 'fim':
        break
    else:
        words_list.append(words)
print(f'Words: {sorted(words_list)}')