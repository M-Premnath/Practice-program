n = int(input("Enter the range: "))
for i in range(1, n+1):
        if i % 5 == 0:
            print("bus",end=" ")
        elif i % 7==0:
            print("7Up",end=" ")
        else:
            print(i,end=" ")

