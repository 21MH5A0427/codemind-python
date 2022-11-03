n=int(input())
s=1
c=0
temp=n
while n>0:
    r=n%10
    for i in range(1,r+1):
        s=s*i
    d=s
    s=1
    c+=d
    n=n//10
if c==temp:
    print("The number",temp,"is a strong number")
else:
    print("The number",temp,"is not a strong number")