n=input()
c=0
for i in n:
    if i.isdigit()==True:
        c=c+1
if c==0:
    print("Doesn't contain digit")
else:
    print("Contains",c,"digit")