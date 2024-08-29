#getting input from the user for which table
a=int(input("Which Table you want to print--->\t"))

# Heading line
print("\n Multiplication Table of \"",a ,"\"\n")

#condition for table 
for i in range(1,11):
    #output
    print ("\t",a,"x",i,"=",a*i)
    
print() #new line at the end