n = 11
for i in range(1,n):
    print("".join([str(x*i).rjust(5) for x in range(1,n)]))