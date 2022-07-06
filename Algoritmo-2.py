print('Digite 6 números inteiros:')
numbers = []
for i in range(1,6+1):
  number = int(input(f'{i} - Digite um número inteiro: '))
  numbers.append(number)
incidents = (numbers.sort()).count(numbers[0])
print(f'O menor número é {numbers[0]} e ele aparece {incidents} vezes')