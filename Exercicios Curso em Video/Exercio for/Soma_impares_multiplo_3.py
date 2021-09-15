#Faça um progrma que calcula a soma entre todos os numeros impares que sao 
#MULTIPLOS DE TRÊS e que se encotram no intervalo de 1 ate 500
soma = 0
cont = 0

for c in range(1, 501, 2):
    if c % 3 == 0:
       
        soma += c
        cont += 1

print (f' A soma de todos os {cont} valores solicitados é {soma}')