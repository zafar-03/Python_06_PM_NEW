# WAP to Check given Number is Positive.

# num = int(input("Enter Value (integer) : "))

# if(num > 0):
#    print("Number is",num)
#    print("Number is Positive!!")

"""
if-else Statement : 
if(condition):
  code1 
else:
  code2

"""
# WAP to Check given Number is Positive or Negative.
# if(num > 0):
#    print("Number is",num)
#    print("Number is Positive!!")
# else:
#    print("Number is",num)
#    print("Number is Negative!!")



"""
Show : (garba)

pass available  entry
pass X        no entry
"""


"""
ladder if-else statement  / elif statement

if(condition):
  code1 
elif(codition2):
  code3
else:
  code2
"""
# WAP to Check given Number is Positive or Negative or Zero.
# if(num > 0):
#    print("Number is",num)
#    print("Number is Positive!!")
# elif(num == 0):
#   print("Number is Zero.")
# else:
#    print("Number is",num)
#    print("Number is Negative!!")


# WAP to Check Which number is Greater
# user 3
# num1 = int(input("Enter the value of num1 :"))
# num2 = int(input("Enter the value of num2 :"))

# if(num1>num2):
#   print("Number1 is Greater !!")
# elif(num1==num2):
#   print("Number1 and Number2 are Equal.")
# else:
#   print("Number2 is Greater !!")


# Nested If Else : 

num1 = int(input("Enter the value of num1 :"))
num2 = int(input("Enter the value of num2 :"))
num3 = int(input("Enter the value of num3 :"))

if(num1>num2):
  if(num1 > num3):
    print("Number1 is Greater !!")
  elif(num1 == num3):
    print("Number1 and Number3 are Equal and Greater.")
  else:
    print("Number3 is Greater !!")
    
elif(num1==num2):
  if(num1 > num3):
    print("Number1 and Number2 are Equal and Greater.")
  elif(num1 == num3):
    print("All are Equal.")
  else:
    print("Number3 is Greater !!")
  
else:
  if(num2 > num3):
    print("Number2 is Greater !!")
  elif(num2 == num3):
    print("Number2 and Number3 are Equal and Greater.")
  else:
    print("Number3 is Greater !!")
