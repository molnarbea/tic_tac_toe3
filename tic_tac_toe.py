import random


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


def geplepes(lista):
        sor = random.randint(0,2)
        oszlop = random.randint(0,2)
        
        i = sor * 3 + oszlop
        while lista[i]!="":
                sor = random.randint(0,2)
                oszlop = random.randint(0,2)
                i = sor * 3 + oszlop
        
        lista[i]="O"
        return lista

def jatekoslepes(lista):
        sor = int(input("Melyik sor: "))
        oszlop = int(input("Melyik oszlop: "))
    
        i = (sor-1) * 3 + (oszlop-1)
        while lista[i]!="":
                print("Ez már foglalt!")
                sor = int(input("Melyik sor: "))
                oszlop = int(input("Melyik oszlop: "))
                i = (sor-1) * 3 + (oszlop-1)
        
        lista[i]="X"
        return lista

def ellenorzes_sor(lista,vegevan):
        i=0
        sor=""
        while len(lista)>i:
                if lista[i]=="":
                        sor+="_"
                sor+=lista[i]
                if i==2 or i==5:
                        sor+="@"
                i+=1
        if "XXX" in sor:
                vegevan=1
        elif "OOO" in sor:
                vegevan=2
        elif "_" not in sor:
                vegevan=3
        
        return vegevan

def ellenorzes_oszlop(lista,vegevan):
        oszlop=""
        cv=0
        if vegevan==0:
                while len(oszlop)<3:
                        if cv%3==0:
                                if lista[cv]=="":
                                        oszlop+="_"
                                else:
                                        oszlop+=lista[cv]
                        cv+=1
                oszlop+="@"
                cv=0
                while len(oszlop)<7:
                        if cv%3==1:
                                if lista[cv]=="":
                                        oszlop+="_"
                                else:
                                        oszlop+=lista[cv]
                        cv+=1
                oszlop+="@"
                cv=0
                while len(oszlop)<11:
                        if cv%3==2:
                                if lista[cv]=="":
                                        oszlop+="_"
                                else:
                                        oszlop+=lista[cv]
                        cv+=1
                if "XXX" in oszlop:
                        vegevan=1
                elif "OOO" in oszlop:
                        vegevan=2
                elif "_" not in oszlop:
                        vegevan=3
        return vegevan

def ellenorzes_atlo(lista,vegevan):
        atlo=""
        i=0
        if vegevan==0:
                while len(atlo)<3:
                        if i%4==0:
                                if lista[i]=="":
                                        atlo+="_"
                                else:
                                        atlo+=lista[i]
                        i+=1
                atlo+="@"
                i=0
                while len(atlo)<7:
                        if i%2==0 and i!=0:
                                if lista[i]=="":
                                        atlo+="_"
                                else:
                                        atlo+=lista[i]
                        i+=1
                if "XXX" in atlo:
                        vegevan=1
                elif "OOO" in atlo:
                        vegevan=2
                elif "_" not in atlo:
                        vegevan=3
        return vegevan

def jatekvege(vegevan):
        if vegevan==1:
                return "Gratulálok, nyertél!"
        elif vegevan==2:
                return "Sajnálom, vesztettél!"
        elif vegevan==3:
                return "Senki nem nyert!"

