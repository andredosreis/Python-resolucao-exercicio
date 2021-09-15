from  random import randint
from  time import  sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)


print('-=' *11)
print(''' Suas opções
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
print('-=' *11)
jogador = int(input('Qual a sua Jogaga? '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)

print (f'O Computador Jogou {itens[computador]}')
print (f'O Jogador Jogou {itens[jogador]} ')

if computador == 0: #Pedra 
    if jogador == 0:
        print ('EMPATE')
    elif jogador == 1:
        print(' Jogador VENCEU')
    elif jogador == 2:
        print(' Computador VENCEU')
    else:
        print('Entrada invalida')

elif computador == 1: #Papel
    if jogador == 0:
        print ('Jogador VENCEU')
    elif jogador == 1:
        print(' EMPATE')
    elif jogador == 2:
        print(' Computador VENCEU')
    else:
        print('Entrada invalida')


elif computador == 2: # Tesoura
    if jogador == 0:
        print ('Jogador VENCEU')
    elif jogador == 1:
        print('Computador VENCEU')
    elif jogador == 2:
        print(' EMPATE')
    else:
        print('Entrada invalida')