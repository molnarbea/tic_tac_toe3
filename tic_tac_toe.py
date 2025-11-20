import random

vegevan=0
lista=["","","","","","","","",""]

lista=["","","","","","","","",""]
def tabla_sor(minta):
        print(minta*10)
def tabla_oszlop(minta,lista1, lista2, lista3):
        print(f"{minta}{lista1:>{1}}{minta:>{2}}{lista2:>{1}}{minta:>{2}}{lista3:>{1}}{minta:>{2}}")
def kiir(lista):
        tabla_sor("*")
        tabla_oszlop("*",lista[0],lista[1],lista[2])
        tabla_sor("*")
        tabla_oszlop("*",lista[3],lista[4],lista[5])
        tabla_sor("*")
        tabla_oszlop("*",lista[6],lista[7],lista[8])
        tabla_sor("*")

while vegevan==0:
       kiir(lista)
       vegevan+=1

    




def geplepes(lista):
    sor = random.randint(0,2)
    oszlop = random.randint(0,2)
    
    i = sor * 3 + oszlop
    lista.insert(i, "O")
    lista.pop(i+1)
    
    print(lista)

geplepes(lista)
