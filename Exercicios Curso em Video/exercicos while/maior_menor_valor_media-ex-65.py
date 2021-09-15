from typing import NoReturn


resp = 'S'
num = soma = quant = media = maior = menor = 0

while resp in 'Ss':
    num = int(input('Digite um numero '))
    soma += num
    quant += 1
    if quant == 1: #para calcular o maior  e menor valor
        maior = menor = num
        #Aqui o primeiro num que eu digitar ele é maior e menor, pois é o primeiro numero digitado
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]# em ordem em explicação, letra maiuscula, sem espaço e o primneira letra 
media = soma / quant
print(f'Voce digitou {quant} numeros e a media foi {media} ')
print(f'O maior valor foi {maior} e o menor foi {menor}')