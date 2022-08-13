# QUESTION 1
rate = int(input("Enter the rate in % "))
priciple = int(input("Enter the principle in kshs "))
time = int(input("Enter the time in years "))

def simple_interest():
    interest = priciple * rate * time /100
    return interest
print("The simple interest is : ", simple_interest())


# QUESTION 2
x = int(input("Enter first integer "))
y = int(input("Enter second integer "))

def sum():
    z = x + y 
    return z
sum()
if sum() >= 15 and sum() <= 20:
        print(20)
else:
        print(sum())

# QUESTION 3
length = int(input("Enter the length in cm"))
width = int(input("Enter the width in cm"))
def area():
    a = length * width
    return a 
print("The area is ", area())

def perimeter():
    p = 2*length + 2*width
    return p 
print("The perimeter is ", perimeter())