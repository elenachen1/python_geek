#Напишите программу, которая по заданному номеру четверти, показывает
#  диапазон возможных координат точек в этой четверти (x и y).

print("Введите номер четверти")

num = int(input())


if ( num <= 0 or  num >= 5 ):
    print("Недопустимое значение")

else:
    if ( num == 1):
        print(" 0 < x < inf , 0 < y < inf")
    elif ( num == 2):
        print("-inf < x < 0 , 0 < y < inf")
    elif ( num == 3):
        print("-inf < x < 0 , -inf < y < 0")
    elif ( num == 4):
        print("0 < x < inf , -inf < y < 0")