list_3n = []
list_5n = []
list_15n = []
list_total = []

i = 0

while (i < 1000):
    if i % 3 == 0:
        list_3n.append(i)
    elif i % 5 == 0:
        list_5n.append(i)
    elif i % 15 == 0:
        list_15n.append(i)
    i = i + 1

a = sum(list_3n)
b = sum(list_5n)
c = sum(list_15n)

print(a)
print(b)
print(a + b - c)
