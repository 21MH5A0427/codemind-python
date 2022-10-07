n=int(input())
n0=0
n1=1
print(n0,n1,end=" ")
for i in range(2,n):
    n2=n0+n1
    n0=n1
    n1=n2
    print(n2,end=" ")
    