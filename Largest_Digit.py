n=int(input())
c=0
while n>0:
    r=n%10
    if r>c:
        c=r
    n=n//10
print(c)