'''Faça um algoritmo que leia 3 números inteiros 
distintos e escreva o menor deles.'''
first = int(input('Enter a first number: '))
second = int(input('Enter a second number: '))
third = int(input('Enter a third number: '))
if ((first > second) and (first > third)):
    print ('The biggest number is', first)
if ((second > first) and (second > third)):
    print ('The biggest number is', second)
if ((third > second) and (third > first)):
    print ('The biggest number is', third)