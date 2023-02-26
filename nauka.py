import random

list0 = []
list1 = []
list2 = []
list3 = []
list4 = []
list5 = []
list6 = []
list7 = []
list8 = []
list9 = []


def rand(list):

    for x in range(1,11):
        y = (random.randint(0, 1000))
        list.append(y)

rand(list0)
rand(list1)
rand(list2)
rand(list3)
rand(list4)
rand(list5)
rand(list6)
rand(list7)
rand(list8)
rand(list9)

print(list0)
print(list1)
print(list2)
print(list3)
print(list4)
print(list5)
print(list6)
print(list7)
print(list8)
print(list9)

lists = (list0, list1, list2, list3, list4, list5, list6, list7, list8, list9)
for3 = []
for2 = []
prime = []
for y in lists:
    for x in y:
        if x % 3 == 0:
            for3.append(x)
        else: pass

for y in lists:
    for x in y:
        if x % 2 == 0:
            for2.append(x)
        else: pass

for y in lists:
    for x in y:

        true = 1

        if (x == 1):
            true = 0

        if (x % 2 == 0) and (x != 2):
            true = 0

        d = 3
        while (d*d<=x) and true == 1:
            if x%d == 0:
                true = 0
            d = d+2

        if true==1:
            prime.append(x)
        else:pass


print("Liczby pierwsze: ")
print(prime)
print("Przez 2 dzielą się: ")
print(for2)
print("Przez 3 dzielą się: ")
print(for3)
