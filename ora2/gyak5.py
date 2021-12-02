import math
a = int(input("Adja meg az (a) számot: "))
b = int(input("Adja meg az (b) számot: "))
c = int(input("Adja meg az (c) számot: "))
diszk = b*b-4*a*c
x1 = (-1 * b + math.sqrt(diszk)) // 2 * a
x2 = (-1 * b - math.sqrt(diszk)) // 2 * a
print(x1, "=x1", x2, "=x2")