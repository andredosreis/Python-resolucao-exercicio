# Desenvolva um programa que leia SEIS NUMOROS INTERIOS e mostre a soma apenas daquelas que forem
# PARES. Se o valor ditado for IMPAR, desconsidere-o.
soma = 0
cont = 0 # ele serve como aculmulador 
for i in range (1, 3):
    num = int(input(f'Digite um numero o {i} '))
    if num % 2 == 0:
        soma += num # soma = soma + num
        cont += 1 # cont = cont + 1
print(f'Voce informou {cont} numeros PARES e a soma foi {soma}')
   