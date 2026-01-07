import tic_tac_toe

vegevan=0
lista=["","","","","","","","",""]

while vegevan==0:
       lista=tic_tac_toe.geplepes(lista)
       print("A gép választása")
       tic_tac_toe.kiir(lista)
       vegevan=tic_tac_toe.ellenorzes_sor(lista,vegevan)
       vegevan=tic_tac_toe.ellenorzes_oszlop(lista,vegevan)
       vegevan=tic_tac_toe.ellenorzes_atlo(lista,vegevan)
       if vegevan==0:
              print("Te jössz.")
              lista=tic_tac_toe.jatekoslepes(lista)
              tic_tac_toe.kiir(lista)
              vegevan=tic_tac_toe.ellenorzes_sor(lista,vegevan)
              vegevan=tic_tac_toe.ellenorzes_oszlop(lista,vegevan)
              vegevan=tic_tac_toe.ellenorzes_atlo(lista,vegevan)
nyertes=tic_tac_toe.jatekvege(vegevan)
print(nyertes)
