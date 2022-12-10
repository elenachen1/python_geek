# Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
print ( "Введите значения 0 или 1 ")
print ("x = ")
x = bool(input())
print ("y = ")
y = bool(input())
print ("z = ")
z = bool(input())

if ( not( x or y or z ) == (not x and not y and not z)):
    print("Выражение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z истинно ")

else:
    print("Выражение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z ложно")