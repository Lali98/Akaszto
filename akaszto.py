import random
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

def main():
    helysegek = beolvas("helyek.txt")
    feladat = random.choice(helysegek)
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
            
      
main()