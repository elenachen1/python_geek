import random
from random import Random, randint


N = int(input())
numbers = [random.randint(-N,N+1) for i in range(N)]
  
result = 1


while True:
    s = input()
    if s == "":
        break
    result *= numbers[int(s)]

print(result)