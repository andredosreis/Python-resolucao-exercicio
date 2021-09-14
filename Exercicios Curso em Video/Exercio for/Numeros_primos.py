num = int(input('Digite um número? '))

cont = 0

for i in range (1, num + 1):

  if num % i == 0:
        print('\033[34m', end= '')
        cont += 1
  else:
        
           
        print('\033[31m', end= '')    
  print(f'{i}', end='')

print(f'\n\033[m0 numero {num} foi divisivel {cont} vezes')
if cont == 2:
   print('E por isso É PRIMO')
else:
       print('E por isso que Não é Primo')
