# 3. TNRS (take nothing return something)
"""
Syntax : 

1. function creation :
def functioname():
    //code (optional)
    return something

2. function calling / use function / invoked function :

a. direct use return 
b. return > store(variable)
"""
def pi():
    return 3.14


# pi()

# Write a program to find area of Circle.
# r*r 
# r**2
# print("Area of Circle : ",pi()*pow(5,2))

# print(5*5)
# print(5**2)
# print(pow(5,2))

# VALUE_PI = pi()
# print(VALUE_PI)


# ======================================
# 4. TSRS (take something return something)
"""
Syntax : 

1. function creation :
def functioname(data):
    //code
    return something

2. function calling / use function / invoked function :
functioname(value)
a. direct use return 
b. return > store(variable)
"""
def result(marks):
    if(marks>35):
        return "Pass"
    else:
        return "Fail"


print(result(90))
print(result(7))
