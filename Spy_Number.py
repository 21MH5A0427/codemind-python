n=int(input())
c=0
s=1
while n>0:
    r=n%10
    c+=r
    s*=r
    n=n//10
if c==s:
    print('Spy Number')
else:
    print('Not Spy Number')
    