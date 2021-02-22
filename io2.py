import sys
lista = []
aux = 0
for line in sys.stdin:
    MAX = line.rstrip()
    break
for line in sys.stdin:
    aux = aux + 1
    lista.append(line.rstrip())
    if int(MAX) <= aux:
        break

print ("Hay %s lineas" % len(lista))
print (lista)  
