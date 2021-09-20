from random import randint
while True:
    jogador = int(input('Diga um valor:'))
    computador = randint(0, 10)
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar')).strip().upper()[0]
        print 
