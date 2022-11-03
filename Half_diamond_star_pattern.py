a=int(input())
if a<3:
    print("The pattern is not possible")
else:
    for i in range(a):
        for j in range(i+1):
            print("*",end="")
        print()
    for k in range(1,a):
        for l in range(a-k,0,-1):
            print("*",end="")
        print()