num = ([], [])
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}º. valor '))
    if valor % 2 == 0:
        num[0].append(valor)# essa posição do primeiro cochete
    else:
        num[1].append(valor)
print('-=' *30)
num[0].sort()# para orendar os numeros 
num[1].sort()
print(f'Os valores pares digitado foram: {num[0]} ')
print(f'Os valores impares digitado foram: {num[1]} ')
