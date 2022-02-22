'''Escreva um programa que mostre todos os números entre 1 e 100 que 
são múltiplos de 3 e 7.'''

number=0
while number < 100:
    number = number +1
    if (number % 3 == 0 and number % 7 == 0):
        print(number)

