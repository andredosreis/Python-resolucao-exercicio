#Um programa que leia o PESO de 5 pessoas. No final. mostrar qual foi a maior e a menor peso lidos
maior = 0
menor = 0
for p in range (1, 6):
  peso = float(input(f'informe o peso da {p}° pessoa '))
  if p == 1:
    maior = peso
    menor = peso
  else:
    if peso > maior:
      maior = peso
    if peso < menor:
      menor = peso

print(f'O maior peso lido foi de {maior}')
print(f'O menor peso lido foi de {menor}')