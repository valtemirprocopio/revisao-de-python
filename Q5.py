'''Usando arrays, leia 5 números inteiros exiba-os 
ordenados do maior para o menor .'''

size = 6
control = 1
numbers = []
while control < size:
  number = int(input(f'Enter the {control}º number:'))
  control += 1
  numbers.append(number)

ordination = sorted(numbers, reverse=True)
print(f'Numbers ordered from largest to smallest: {ordination}')

