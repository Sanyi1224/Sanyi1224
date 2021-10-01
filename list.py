my_list = [1, 2.5, "alma", False]
print("A lista hossza:", len(my_list))
print("A len() függvény visszatérési értékének típusa", type(len(my_list)))

print("A lista tartalmazza-e a 2.5 értéket:", 2.5 in my_list)
print("Az in operátor eredményének típusa:", type(2.5 in my_list))

print("A lista tartalmazza-e a 2 értéket:", 2 in my_list)
print("Az in operátor eredményének típusa:", type(2 in my_list))

try:
    print("A 2 érték pozíciója a listában:", my_list.index(2))
    print("Az in operátor eredményének típusa:", type(my_list.index(2)))
except ValueError:
    print("hiba")