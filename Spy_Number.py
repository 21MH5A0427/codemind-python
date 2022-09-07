n=list(input())
c=0
s=1
for i in n:
    a=int(i)
    c+=a
    s*=a
if c==s:
    print("Spy Number")
else:
    print("Not Spy Number")