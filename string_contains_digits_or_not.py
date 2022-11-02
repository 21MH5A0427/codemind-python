t=int(input())
for i in range(t):
    n=input()
    c=0
    for i in n:
        if i.isdigit()==True:
            c+=1
    if c==0:
        print("No")
    else:
        print("Yes")