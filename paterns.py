#Enter no of rowa want to print Print("Normal Pattern")
#rows=int(input("Enter no of Rows --->\t"))
rows=3
for i in range(rows):
    #nested loop
    for j in range(i+1):
      print("*",end=" ")
    print()

#PRINT STRING AS A PATTERN
string=input("Enter the string--->\t")
x=0
for i in string:
    x=x+1
    print(string[0:x])
for i in string:
    x=x-1
    print(string[0:x])

