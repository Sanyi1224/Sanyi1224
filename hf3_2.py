num = float(input('Adja meg a termék árát: '))
if num < 10000:
    print(num*0.9, "10%")
else:
    print(num*0.8, "20%")