# String Formatting and Manuplation :

# String :  It's a Collection of Chars.

# Syntax :
# " ", ' ', """ """,''' '''


# Create Empty String Without Chars

# first_name  = 
# print(first_name,type(first_name))


# 2.
# use for Type Casting  + to create a string
# first_name = str()
# print(first_name,type(first_name))


# ====================
# String Formatting : 
# 1.  using f-string : 
# firstname = "Raj"
# lastname = "shah"
# age = 12
# 

# print("Your name is ",firstname," ",lastname,".",sep="")

# print(f"Your name is {firstname} {lastname}.Your age is {age}.")


# 2. using format Method : 
# print("Your name is {1} {0}.Your age is {2}.".format(firstname,lastname,age))
                                                #    0        1       2


# Methods of String : 
# username = "This Is My String."
# print(username)

# # UPPERCASE
# print(username.upper())

# # lowercase
# print(username.lower())

# # title : 
# print(username.title())

# count :
# print(username.count("s"))


# print(username.upper().count("I"))
# print(username.upper().count("I"))


# ============================
data = "Raj"
# print(data)
# print(data*5)

# Decoration : 
# print("="*20)

# print("="*15)



# Loop : 
# for loop :
# mystr = "Hello Everyone,Welcome to PythoN"
                                    # 
# index :   +ve
    #    0123456.........................
# -ve: 
# print(mystr)

# print(mystr[0])
# print(mystr[31])

# print(len(mystr))
# print(mystr[len(mystr)-1])

# print(mystr[-1])



# for char in mystr:
    # print(char)

# mystr = "Hello Everyone,Welcome to PythoN"

# for i in range(0,len(mystr)):
#     print(mystr[i])



# Slicing of String  :
# data = "Hello Everyone,Welcome to PythoN"

# print(data)
# print(data[2])
# print(data[2:])
# print(data[2:5])
# print(data[2:20])
# print(data[2:20:2])




# WRITE A Python Program to Conver GSring in to Uppercase


# data = "data"


# data.upper()