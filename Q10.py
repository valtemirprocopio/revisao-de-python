'''Escreva um programa que leia n números e mostre a soma dos mesmos. 
O programa deve parar de ler quando o usuário digitar -1.'''

n = 0
summation = 0
while n != -1:
    n = int(input('Enter an integer: '))
    if n == -1:
        break
    else:
        summation = summation+n
print(f'Sum of numbers entered: {summation}')