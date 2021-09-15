#Melhore o desesfio 061, perguntado para o usuaria se ele quer mostrar mais alguns termos.
#o programa encerra quando ele disse que quer mostrar 0 termos.

print('Gerador de Pa')
print('=-' *10)
primeiro = int(input('Digite o primeiro termo '))
razao = int(input('Degite a razão '))
termo = primeiro
cont = 1
total = 0 
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} -> ', end=(''))
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos voce deseja mostar mais? '))
print(f'voce mostrou {total} termos')
 



