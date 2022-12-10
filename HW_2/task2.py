a = int(input())
i = 1
j = 1
p = 1

while i <= a:
    for j in range(1,i+1):
        p = p * j
        j+=1
    j = 1
    i+=1
    print(p, end=" ")
    p = 1
   

