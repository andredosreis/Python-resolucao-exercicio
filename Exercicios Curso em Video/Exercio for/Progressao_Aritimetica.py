termo = int(input('Qual o primeiro termo '))
razao = int(input('Qual a razao '))
decimo = termo + (10 - 1) * razao
for i in range (termo, decimo + razao, razao):
    print(f'{i}', end= ' -> ')

print('Acabou')