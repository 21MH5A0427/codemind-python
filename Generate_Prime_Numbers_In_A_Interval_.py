n=int(input())
m=int(input())
for number in range (n, m+ 1):  
    if number > 1:  
        for i in range (2, number):  
            if (number % i) == 0:  
                break  
        else:  
            print (number)  