n=int(input())
a=65
b=n
for i in range(1,n+1):
    for j in range(1):
        ch=chr(a)
        print((ch+" ")*b)
    a+=1
    