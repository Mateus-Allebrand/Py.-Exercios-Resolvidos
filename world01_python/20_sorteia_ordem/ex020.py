#Programa sorteia a ordem que será apresentados os trabalhos da turma.


#Programa principal.
import random
n1 = input('Digite o nome do primeiro aluno: ')
n2 = input('Digite o nome do segundo aluno: ')
n3 = input('Digite o nome do terceiro aluno: ')
n4 = input('Digite o nome do terceiro aluno: ')
lista = [n1,n2,n3,n4]
random.shuffle(lista)
print(lista)
