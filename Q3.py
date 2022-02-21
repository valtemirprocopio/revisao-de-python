'''Escreva um programa leia dois nomes de times de futebol, a quantidade de gols do primeiro time, 
a quantidade de gols do segundo time e mostre o nome do time vencedor da partida.'''



first_team = input('Enter the name of the first team: ')
first_team_goals = int(input('Enter the number of goals of the team ' + first_team + ' :'))

second_team = input('Enter the name of the second team: ')
second_team_goals = int(input('Enter the number of goals of the team ' + second_team + ' :'))

if (first_team_goals > second_team_goals):
    print ('The winning team is ' + first_team)
else:
    print ('The winning team is ' + second_team)