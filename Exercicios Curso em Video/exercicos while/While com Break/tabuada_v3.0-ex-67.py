
cont = mult = 0

while True:
    num = int(input('Qual a tabuada vc quer ver? '))
    if num < 0:

        break

    print('-' *30)
    for c in range(1, 11):

        print(f'{num} x {c} = {num*c}')
    print('-' *30)
   
print('Fim da tabuada kkk')