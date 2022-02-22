'''Escreva um programa que leia um número inteiro n e mostre todos 
os números entre 0 e n.'''
n = int(input('Enter the number:'))
control=0
if n < 0:
    lista = sorted(list(range(n+1,0,1)), reverse= True)
    print(f'Numbers between 0 e {n}: {lista}')
else:
    lista = list(range(1,n,1))
    print(f'Numbers between 0 e {n}: {lista}')
