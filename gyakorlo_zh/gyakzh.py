"""
def valami(x:int,y:int) -> float:
    osszeg = x + y
    return  osszeg

x = int(input("Adjon meg egy számot:"))
y = int(input("Adjon meg még egy számot:"))

print(valami(x,y))
"""

#szavazatok.txt
#for i in range(10)
#for i in range(1,10):
#    print(i)
#for i in range(0,len(lista)):  !!!!!

#,i = 0 i = 1, i = 2, i = 3 .....
#lista[i] == valmaivel?

#lista = [[1,1,1,2],[1,2,3,4],[33,33,3]]

#sor = lista[0] = [1,1,1,2]

#lista[0] = 1112
#for sor in lista:
#    print(sor[0])

#int-ker int-szavazat str-vezetéknév str-utónév str-partrov
def beolvas()->list:
    try:
        lista = []
        f = open("szavazatok.txt","r", encoding="UTF-8")

        for sor in f:

            sor = sor.strip().split()

            sor[0] = int(sor[0])
            sor[1] = int(sor[1])

            lista.append(sor)

        f.close()
    except FileExistsError:
        print("Hiba!")
    return lista

#print(lista)

lista=beolvas()
#print(lista)

#len()
def masodik(lista: list):
    print("Képviselők száma:",len(lista))

#masodik(lista)

def harmadik(lista: list):
    try:
        elonev = input("Kérem az előnevet: ")
        utonev = input("Kérem az utónevet: ")
    except TypeError:
        print("Hiba!")
    benne = False
    for sor in lista:
        if sor[2].lower() == elonev.lower() and sor[3].lower() == utonev.lower():
            print(sor[1],"-",sor[2],sor[3])
            benne = True
            break
    if benne == False:
        print("Nincs ilyen képviselő!")

#harmadik(lista)

def negyedik(lista: list):
    osszlakos = 12345 #szavazásra jogosultak száma
        #A jogosultak hány százaléka ment el szavazni
    szavazok = 0
    for sor in lista:
        szavazok = szavazok + sor[1]
    print("A szavzók aránya: ",round((szavazok/osszlakos)*100,2),"%",sep="")

#negyedik(lista)

def otodik(lista: list):
    partok = []
    for sor in lista:
        if sor[4] not in partok:
            partok.append(sor[4])
    #print(partok) --> 5db
    part_szav = [0,0,0,0,0]

    for sor in lista:
        if sor[4] == "-":
            part_szav[0] += sor[1]
        if sor[4] == "GYEP":
            part_szav[1] += sor[1]
        if sor[4] == "HEP":
            part_szav[2] += sor[1]
        if sor[4] == "ZEP":
            part_szav[3] += sor[1]
        if sor[4] == "TISZ":
            part_szav[4] += sor[1]
    #print(part_szav)

#otodik(lista)

def hatodik(lista: list):
    max_votes = 0
    for sor in lista:
        if sor[1] > max_votes:
            max_votes = sor[1]
    for sor in lista:
        if sor[1] == max_votes:
            print("A legtöbb szavazatot kapók:",sor[1],"-",sor[2],sor[3],"-",sor[4])
#hatodik(lista)

def hetedik(lista: list):
    f = open("kepviselok.txt","w",encoding="UTF-8")

    keruletek = []
    for sor in lista:
        if sor[0] not in keruletek:
            keruletek.append(sor[0])
    keruletek.sort()

    #print(keruletek)

    for elem in keruletek:
        max = 0
        for sor in lista:
            if sor[0] == elem:
                if sor[1] > max:
                    max = sor[1]

        for sor in lista:
            if sor[1] == max and sor[0] == elem:
                f.write(str(sor[0]) + " " + sor[2] + " " + sor[3] + " "+"\n")
                if sor[4] == "-":
                    f.write("független\n")
                else:
                    f.write(sor[4]+"\n")
    f.close()

hetedik(lista)








