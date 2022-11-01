def ispal(n):
    t=n
    s=0
    while t:
        r=t%10
        t=t//10
        s=s*10+r
    if s==n:
        return True
    else:
        return False
n=int(input())
while True:
    a=str(n)
    a=int(a[::-1])
    n=n+a
    if ispal(n):
        print(n)
        break