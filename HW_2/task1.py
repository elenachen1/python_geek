a = input()

def sum_a(a):                           
    if float(a) < 0:                           
        a = float(a) * (-1)
        print(a)
    num = 0

    for i in str(a):
        if i != '.':
            num += int(i)
    return int(num)

   
print(sum_a(a))