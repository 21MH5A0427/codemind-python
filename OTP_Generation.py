n=input()
b=n[::-1]
a=int(b)
while a>0:
    r=a%10
    if r%2==1:
        c=r**2
        f=str(c)
        print(f,end="")
    a=a//10