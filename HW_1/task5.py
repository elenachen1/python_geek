#Напишите программу, которая принимает на вход координаты 
# двух точек и находит расстояние между ними в 2D пространстве.

#Пример:

#- A (3,6); B (2,1) -> 5,09
#- A (7,-5); B (1,-1) -> 7,21

import math

a_x = int(input())
a_y = int(input())
b_x = int(input())
b_y = int(input())
print(round(math.sqrt(pow(a_x - b_x,2)+ pow( a_y - b_y,2)),2))