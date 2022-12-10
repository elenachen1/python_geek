#Реализуйте алгоритм перемешивания списка.

import random
list = []

while True:
    s = input()
    if s == "":
        break
    list.append(s)
print(f"исходный список:\n {list}")
for i in range(0,len(list)):

    if (i == len(list)-1):
        
        list[i] = list[i]

    else:
        if (int(list[i]) % 2 == 0):
            a = list[i]
            b = list[i - 1]
            list[i] = b
            list[i - 1] = a
        else:

            a = list[i]
            b = list[i + 1]
            list[i] = b
            list[i+1] = a

print(f"список после перемешивания:\n{list}")