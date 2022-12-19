'''
Uma vez que o fatorial é uma função, use a função para calcular a combinação e arranjo 
de dois números. Relembrando que:
'''

def Fat(num):
    if num <= 1:
        return 1
    else:
        num = num * Fat(num - 1)

    return num


n1, n2 = input('-> ').split(' ')
n1, n2 = int(n1), int(n2)
Arrajo = int(Fat(n1) / Fat(n1 - n2))
Combinação = int(Fat(n1) / (Fat(n2) * Fat(n1 - n2)))
print(
    f' O Arranjo de {n1} e {n2} é : {Arrajo} \n A Combinação de {n1} e {n2} é : {Combinação}')
