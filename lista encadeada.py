import random

lista = []

class no ():
    def __init__(self, valor = None, proximo = None):
        self.valor = valor;
        self.proximo = proximo;


def criandoLista () :
    x = input("Quantos elementos terá a lista: ")
    contador = 0;
    while contador < int(x): 

        elemento = input("Valor do elemento: ")
        lista.append(no(elemento))

        if contador > 0:
            lista[contador - 1].proximo = lista[contador].valor
        
        contador += 1



criandoLista()
for x in lista:
    print(x.valor)

print("\n")

random.shuffle(lista)
4
for x in lista:
    print(x.valor)
    print(x.proximo)
    print("\n")