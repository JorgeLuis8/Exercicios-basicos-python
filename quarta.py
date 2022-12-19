'''
Faça um programa para calcular o fatorial de um número, o código do fatorial deve ser 
uma função. Faça o fatorial de duas formas: a. iterativa e recursiva
'''

def FatIterativo(num):
    fatorial = 1

    for c in range(2, num + 1):
        fatorial *= c

    return fatorial


def fatRecursivo(num):
    if num <= 1:
        return 1
    else:
        num = num * fatRecursivo(num - 1)
        return num


print(FatIterativo(int(input('Fatorial iterativo: '))))
print(fatRecursivo(int(input('Fatorial recursivo '))))
