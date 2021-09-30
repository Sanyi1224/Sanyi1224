g = str(input("Adja meg a felhasználó nemét(m=fiú/f=lány): "))
proceed = "f"
if g == proceed:
    k = float(input("Adja meg a felhasználó korát: "))
    if k >=10 and k <=12:
        print("A felhasználó felvéve!")
    else:
        print("A felhasználó nem lett felvéve!")
else:
    print("A felhasználó nem lett felvéve!")