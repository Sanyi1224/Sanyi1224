file = open("lorem.txt", "r")
adat = file.read()
karakterek_szama = len(adat)
print('Karakterek száma a fájlban:', karakterek_szama)
line_count = 0
for line in file:
    if line != "\n":
        line_count += 1
file.close()
print("Sorok száma:", line_count)