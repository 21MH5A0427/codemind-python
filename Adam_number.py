n=int(input())
t=n
s=n**2
d=0
e=0
while n>0:
    r=n%10
    d=(d*10)+r
    n=n//10
a=d**2
while a>0:
    q=a%10
    e=(e*10)+q
    a=a//10
if e==s:
    print("True")
else:
    print("False")