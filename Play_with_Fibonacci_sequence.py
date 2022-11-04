n=int(input())
f=0
f1=1
if n<=0:
    print(f)
else:
    print(f,f1,end=" ")
    for i in range(2,n):
        ne=f+f1
        print(ne,end=" ")
        f=f1
        f1=ne