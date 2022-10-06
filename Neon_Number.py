n=int(input())
s=n**2
c=0
while s>0:
    r=s%10
    c+=r
    s=s//10
if c==n:
    print("Neon Number")
else:
    print("Not Neon Number")
        