number = 10
if number%2==0:
    print("A szám páros.")
else:
    print("A szám páratlan.")

number2 = 30
if number % number2 == 0:
    print("A", number2, "osztója a", number)
else:
    if number2 % number == 0:
        print("A", number, "osztója a", number2)
    else:
        print("Egyik sem osztója a másiknak.")

str = "alma"
if str[0] == str[-1]:
    print("Az első utolsó karakter megegyezik.")
else:
    print("Az első utolsó karakter nem egyezik meg.")
    
if number > 0:
    print("pozitiv")
if number < 0:
    print("negativ")
if number == 0:
    print("nulla")

if str[0].isupper():
    print("Nagybetűvel kezdődik.")
else:
    print("Nem nagybetűvel kezdődik.")
    
str2 = "almafa"
str = "almaszár"
if str[0:5] == str2[0:5]:
    print("Az első 5 karakter azonos.")
else:
    print("Nem azonos az első 5 karakter.")