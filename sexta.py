'''
Faça uma função que receba um número inteiro e retorne verdadeiro caso ele seja primo e 
falso caso contrario. Em seguida, faça um código que leia dois números inteiros e positivos 
e calcule e exiba todos os números primos entre o intervalo formado por esses números. 
Caso não exista nenhum número primo dentro desse intervalo exiba a mensagem “Não 
existe nenhum número primo dentro desse intervalo”
'''

def primo(num):
    list = []
    aux = num

    while aux >= 1:
        if num % aux == 0:
            list.append(aux)

        aux -= 1

    if len(list) == 2:
        return True
    else:
        return False


n1, n2 = input('Digite os números: ').split(' ')
n1, n2 = int(n1), int(n2)
lista = []

for c in range(n1, n2 + 1):
    if primo(c):
        lista.append(c)

print(f'Números primos entre {n1} e {n2} são : {lista}') if lista else print(
    'Não existe nenhum número primo dentro desse intervalo')
