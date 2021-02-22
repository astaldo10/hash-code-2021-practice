import sys
from copy import copy

# lectura de la entrada de datos
def read_file(input):
    
    mesas = { 2: 0, 3: 0, 4: 0}
    n_pizzas = 0
    pizzas = []
    ingredients = []
    read_pizza = False

    for line in input:
        if read_pizza:
            data = str(line.rstrip()).split(" ")
            ingredients = ingredients + data[1:]
            pizzas.append(str(line.rstrip()).split(" "))
        else:
            data = str(line.rstrip()).split(" ")
            mesas_tipo = data[1:]
            mesas = { k: int(mesas_tipo[k - 2]) for k in mesas.keys() }
            n_pizzas = int(data[0])
            read_pizza = True

    ingredients_p = list(set(ingredients))
    ingredients_p.sort()
    print(mesas)
    print(pizzas)

    return mesas, n_pizzas, ingredients_p, pizzas

# calculo de valor de una pizza por aparicion de sus ingredientes 
def pizza_value(pizza, ingredients, occurences):
    final_value = []
    for i in range(len((ingredients))):
        final_value.append(float(pizza[i]) / occurences[i])
    return final_value

# resultado del programa
# expected -> output([[1,4],[0,2,3]])
def output(tuples):
    print(len(tuples))
    for tuplez in tuples:
        tuplez = [str(len(tuplez))] + tuplez
        print (" ".join(map(str, tuplez)))
    return


# hilo de ejecucion del programa
if __name__ == "__main__":

    mesas, n_pizzas, ingredients, pizzas = read_file(sys.stdin)

    table = []

    # inserta en table las pizzas como listas de aparicion de ingredientes
    for pizza in pizzas:
        l = []
        for p in ingredients:
            if p in pizza[1:]:
                l.append(1)
            else:
                l.append(0)
        table.append(l)
        
    print(table)

    # conteo de apariciones de ingredientes por orden
    tt = [sum([x[i] for x in table]) for i in range(len(table[0]))]
    print (tt)

    # calculo de valor de las pizza por aparicion de sus ingredientes
    for i in range(len(table)):
        table[i] = pizza_value(table[i], ingredients, tt)

    print (table)

        