from queue import Queue

lista = Queue(maxsize= 10) ## posso definir um tamanho máximo

lista.put(10)
lista.put(30)
lista.put(90)

print(lista.full()) ## Serve para eu saber se a listra está no máximo
print(lista.empty()) ## Consigo saber se a lista está vazia
print(lista.get()) ## Consigo remover um elemento específico
 
## Se eu quiser visualizar a lista:
lista_X = []
while not lista.empty():
    lista_X.append(lista.get())
print(lista_X)