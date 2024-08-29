# Find the given number is odd or even using if else program

#getting input from the user
a=int(input("Enter number a....."))
b=int(input("Enter number b......"))

#using if else function
if a % 2 == 0:
    print(a,"is even number")
else:
    print(a,"is odd number")

#add two num and chech odd or even
c =a+b
if c % 2 == 0:
    print(("after addition "), c ,(" is even"))
else:
    print(("after addition "), c ,(" is odd"))
  