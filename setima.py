'''
Faça um programa que receba um valor em decimal e o converta em binário. Para fazer 
este programa use apenas divisões por 2. Não utilize nenhuma função que faça esta 
conversão automática.
'''

def convertDecimalBinario(decimal):
    Bin = ''
    while decimal > 0:
        Bin += str(decimal % 2)
        decimal //= 2
    return Bin[::-1]


num = int(input('Digite um número: '))
print(f'{num} Convertido para bináirio é '+convertDecimalBinario(num))
