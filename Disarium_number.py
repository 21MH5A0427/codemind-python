n=int(input())
s1=len(str(n))
temp=n
c=0
s=1
while n>0:
    r=n%10
    s=r**s1
    c+=s
    s1-=1
    n=n//10
if c==temp:
    print("True")
else:
    print("False")