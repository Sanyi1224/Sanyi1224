import random

number = 5
if number >= 3 and number < 17:
    print("Beleesik a szám a (3,17) intevallumba.")
else:
    print("Nem esik bele a szám a (3,17) intevallumba.")
    
a, b , c = 2, 3, 4
if a+b>c and a+c>b and b+c>a:
    print("Lehet háromszöget szerkeszteni a megadott számokból.")
else:
    print("Nem lehet háromszöget szerkeszteni a megadott számokból.")
    
if a > b and a > c:
    print(a," a legnagyobb")
elif b > a and b > c:
    print(b," a legnagyobb")
elif c > a and c > b:
    print(c," a legnagyobb")
    
if a < b and a < c:
    print(a," a legkisebb")
elif b < a and b < c:
    print(b," a legkisebb")
elif c < a and c < b:
    print(c," a legkisebb")
    
character = "a"
magánhangzók = "aáeéiíoóöőuúüűAÁEÉIÍOÓÖŐUÚÜŰ"
if magánhangzók.find(character) >= 0:
    print(character, "magánhangzó")
else:
    print(character, "mássalhangzó")
    
number = 30
if number % 3 == 0 and number % 5 == 0:
    print("Osztható 3-al is és 5-tel is")
elif number % 3 == 0:
    print("Csak 3-al osztható.")
elif number % 5 == 0:
    print("Csak 5-tel osztható.")
else:
    print("Nem osztható sem 3-al, sem 5-tel")
    
grade = random.randint(1, 5)
if grade == 5:
    print("kiváló")
elif grade == 4:
    print("jó")
elif grade == 3:
    print("közepes")
elif grade == 2:
    print("elégséges")
elif grade == 1:
    print("elégtelen")
    
print(random.random())

number1 = int(input("Adjon meg egy számot: "))
if number1 > 10:
    print(number1, "nagyobb, mint 10.")
elif number1 == 10:
    print(number1, "egyenlő 10-el.")
elif number1 < 10:
    print(number1, "kisebb, mint 10.")