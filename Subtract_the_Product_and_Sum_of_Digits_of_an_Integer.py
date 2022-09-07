n=list(input())
c=0
s=1
for i in n:
    a=int(i)
    s*=a
    c+=a
print(s-c)
    