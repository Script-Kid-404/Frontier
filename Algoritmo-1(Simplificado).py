#   Média Final   #

print('--- Média Escolar ---')
# Input / Entrada:
n1, n2, n3 = map(float, input('Digite as (3) notas do aluno para obter a Média Final: ').split())
media = (n1*2 + n2*3 + n3*5) / 10 # calculation / cálculo da média
# Output / Saída:
print(f'A Média Final do aluno é: {media:.2f}')