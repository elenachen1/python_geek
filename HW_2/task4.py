import random
from random import Random, randint


N = int(input())
numbers = [random.randint(-N,N+1) for i in range(N)]
    


f = open('file.txt', 'w')
while True:
    s = input()
    if s == "":
        break
    f.write(s+"\n")
f.close()

result = 1
f = open('file.txt', 'r')
for line in f:
    if line == "":
        break
    result *= numbers[int(line)]
f.close()
print(result)