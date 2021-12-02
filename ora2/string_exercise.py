python = "python"
print("A python szó 1. karaktere:", python[0])
print("A python szó utolsó karaktere:", python[-1])
print("A python szó utolsó karaktere:", python[len(python) - 1])
str2 = "hallgató"
str3 = "Hiába a hegynyi anyag, a hallgató gyorsan halad."
str2_position_in_str3 = str3.find(str2)
print(str3[str2_position_in_str3:str2_position_in_str3 + len(str2)])
str4 = "Elemi"
str5 = "programozás"
str6 = str4 + " " + str5
print(str4, str5)
print(str6)
str7 = "péntek van"
print ((str7[0:6] + " ")* 7)
str8 = "hegy"
str9 = "tananyag"
if str8 in str3:
    print("A hegy szó benne van str3-ban.")
if str8 not in str3:
    print("A hegy szó nincs benne str3-ban.")
if str9 in str3:
    print("A tananyag szó benne van str3-ban.")
if str9 not in str3:
    print("A tananyag szó nincs benne str3-ban.")
str10 = "alma"
str11 = "Alma"
if str10 == str11:
    print("Azonosak.")
else:
    print("Nem azonosak.")
eredmeny = str10 > str11
print(eredmeny)