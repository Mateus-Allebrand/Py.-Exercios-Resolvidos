#Contrua um programa que leia um número inteiro n e mostre a sequancia de número fibonates ate esse númeor n
n = int(input('Digite um número: '))
cont = 1
novo = 0
while cont <= n:
    print(cont)
    cont = novo + cont
    novo = cont - novo
    