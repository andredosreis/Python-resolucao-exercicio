#escreva DOIS NÚMEROS inteiros e compare-os, mostrando na tela uma mensagem:
# O PRIMEIRO VALOR é maior
# O SEGUNDO VALOR  é maior
# NAO EXISTE valor maio, os dois são IGUAIS

prim_num = int(input('Digite primeiro numero?'))
seg_num = int(input('digite o segundo numero'))

if prim_num > seg_num:
    print(f'o primeiro numero é maior com o valor {prim_num}')

elif prim_num < seg_num:
    print(f' O segundo numeo é maior com o valor {seg_num}')

elif  prim_num == seg_num:
    print('não existe valor maior ou menor, os dois são IGUAIS')
