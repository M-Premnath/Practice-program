# hint 153 is amstrong num
# input to check
num = int(input("Enter the num you want to check--->\t"))

# Calculation for amstrong num given num x 3 times
amstrong = sum(int(digit)**3 for digit in str(num))

# Conditon for output 
if num == amstrong:
    print(amstrong,"is a Amstrong number")
else:
    print(amstrong,"is Not a Amstrong num")
