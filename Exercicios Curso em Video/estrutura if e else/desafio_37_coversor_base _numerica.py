num = int(input('Digite um numero?'))
print(''' Escolha uma das bases para converção:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')

opcao = int(input('sua opcao'))

if opcao == 1:
    print(f' {opcao} convertido para BINARIO é igual { bin(num)[2:]}')

elif opcao == 2:
    print(f' {opcao} convertido para OCTAL é igual { oct(num)[2:]}')


elif opcao == 3:
    print(f' {opcao} convertido para HEXADECIMAL é igual {hex(num)[2:]}')

elif opcao > 3:
    print('valor invalido')

