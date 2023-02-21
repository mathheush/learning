a = input("Wpisz liczbe do odwrocenia: ")
a = int(a)
y = 0

while (a > 0):
    x = a % 10
    y = (y * 10) + x
    a = a // 10


print(y)
