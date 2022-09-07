t=int(input())
for i in range(t):
    a=int(input())
    b=int(a**(0.5))
    if b**2==a:
        print("True")
    else:
        print("False")