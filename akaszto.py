import random
from fh_gon import *

def beolvas(filenev):
    # ide jön a kód
    lista = []
    forrasfile = open(filenev,mode='r',encoding='UTF-8')
    for sor in forrasfile:
        lista.append(sor.strip())
    forrasfile.close()
    return lista

def feladvany(szo):
    return szo[0] + "." * (len(szo) - 2) + szo[-1]

def cserel(feladvany, szo, betu):
    eredmeny = szo[0]
    for i in range(1, len(szo)-1):
        if szo[i] == betu:
            eredmeny += betu
        else:
            eredmeny += feladvany[i]
    eredmeny += szo[-1]
    return eredmeny

def gep_gondol(lista):
    feladat = random.choice(lista)
    kiirando = feladvany(feladat)
    proba = 6

    print(kiirando)
    while "." in kiirando and proba > 0:
        betu = input("Adj meg egy betut vagy tippej egy város nevet: ")
        if len(betu) > 1:
            if betu.lower() != feladat.lower():            
                proba = 0
            break

        if betu in feladat[1: -1]:
            kiirando = cserel(kiirando, feladat, betu)
        else:
            proba -= 1
            print("A hianyzo betu kozott nem talalhato,", proba, "tipped van meg")            
        print(kiirando)

    if proba > 0:
        print("Gratuálok! Megnyertet a játékot!")
    else:
        print("A tippeit elfogytak, ez kellet volna kitalálni:", feladat)

def fh_gondol(lista):
    print("Gondolj egy magyar településre!")
    kiirando=input("Írd be a feladványt:")
    lehetsegesek = keres(kiirando, lista)
    #print(lehetsegesek)
    # while ciklus inkább, amíg több mint 1 lehetséges van!
    if len(lehetsegesek) == 0:
        print("Nincs ilyen település.")
    elif len(lehetsegesek) == 1:
        print(lehetsegesek[0], "a gondolt város.")
    else:
        print(lehetsegesek)
        # betu = betutipp(kiirando, lehetsegesek[0])
        # valasz = input(f"Van benne '{betu}' betű? (i/n): ")
        # if valasz == "i":
        #     kiirando2=input("Írd be a feladványt:")
        #     while not ellenor(kiirando, kiirando2, betu):
        #         kiirando2=input("Írd be a feladványt:")
        #     lehetsegesek = keres(kiirando, lehetsegesek)
        # else:
        #     lehetsegesek = kizar(lehetsegesek, betu)

def main():
    helysegek = beolvas("helyek.txt")
    gep_gondol(helysegek)

    fh_gondol(helysegek)
    
            
      
main()