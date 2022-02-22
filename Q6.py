'''Leia os dois primeiros números de um array de inteiros e depois calcule 
os 8 números seguintes do array. A regra é que os demais elementos são calculados 
somando os dois anteriores. Exiba o array usando print.'''
numbers = [int(input('Digite o 1º numero:')),int(input('Digite o 2º numero:'))] #adicionando os dois elementos ao array numbers
control=0
for control in range(6):#ate 6 pois já existe dois elementos no array
    numbers.append(numbers[control] + numbers[control+1])#o proximo elemento a ser adicionado é a soma da posiçao zero[0] e posição[1]
    control+=1 # controle de parada
print("Numbers:",numbers)
