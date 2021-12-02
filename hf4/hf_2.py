import math

def N_MT(a, q, N):
    return (a * (int)(math.pow(q, N - 1)))

a = int(input("Adja meg az első elemet: "))
q = int(input("Adja meg a hányadost: "))
N = int(input("Adja meg a keresett elemet: "))

print("Az", N, ".-ik eleme a sorozatnak:",
                            N_MT(a, q, N))