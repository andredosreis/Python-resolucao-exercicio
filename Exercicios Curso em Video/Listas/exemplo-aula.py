galera = list ()
dados = list()
totalmai = totalmen = 0
for c in range(0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])#os dois pontos no cochetes serve para copiar os dados dos Dados
    dados.clear() #que serve que toda vez que terminar o laço limpar os dados

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade ')
        totalmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totalmen += 1

print(f'Temos {totalmai} maiores e menores {totalmen} de idade ')
