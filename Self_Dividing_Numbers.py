m=int(input())
n=int(input())
for i in range(m,n+1):
    c=0
    k=i
    while i>0:
        r=i%10
        i=i//10
        if r!=0:
            if k%r==0:
                c+=1
    if c==len(str(k)):
        print(k,end=" ")
            