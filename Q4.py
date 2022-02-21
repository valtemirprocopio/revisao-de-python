'''Brincadeira do ímpar ou par: escreva um programa que leia dois nomes e dois valores inteiros, 
que correspondem ao que cada um colocou, e informe quem ganhou o “ímpar ou par”.'''


first_name = input('Enter the name of the first team: ')
first_name_number = int(input('Now, '+ first_name +', enter a number: '))

second_name = input('Enter the name of the first team: ')
second_name_number = int(input('Now, '+ second_name +' , enter a number: '))
sum = second_name_number + first_name_number
if (sum % 2 == 0):
    print ('The pair won!')
else:
    print ('The odd won!')