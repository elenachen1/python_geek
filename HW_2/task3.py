
n = int(input())

def pos(n):
    s = 0
    for i in range(1,n+1):
        p=0
        p = (1+(1/i))**i
        s +=p
    return(float(s))

print(pos(n))

