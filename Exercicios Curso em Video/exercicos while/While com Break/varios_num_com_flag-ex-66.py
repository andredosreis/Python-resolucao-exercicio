cont = soma = 0

while True:
    num = int(input('Digite um valor (999) '))
    
    if num == 999:
       
        break
    soma += num
    cont += 1
print(f'voce digitou {cont} vezes e a soma é {soma} ')
