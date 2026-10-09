# Operation : Operators


#   operand1  operator operand2


# 1. Arithmatic Op
"""
+
-
/
//  : floor Division 
*
%   : Modulo/moduler 
**
"""
# num_1 = int(input("Enter Value 1 :"))
# num_2 = int(input("Enter Value 2 :"))

# print("Addition : ",num_1+num_2)
# print("Sub : ",num_1-num_2)
# print("Mul : ",num_1*num_2)
# print("Div : ",num_1/num_2)      # float    12/2  = 6.0  11/2 = 5.5
# print("floor div : ",num_1//num_2) # int    12//2 = 6     11//2 = 5
# print("Modulo : ",num_1%num_2) # div > reminder : modulo  11/2
# print("Expo : ",num_1**num_2)


# 3. Relational Op : return : Boolean(True / False)
"""
< 
>
<=
>=
==
!=    : not equal to
"""
# Condition :
# num_1 = input("Enter Value 1 :")
# num_2 = int(input("Enter Value 2 :"))

# print(num_1 < num_2)
# print(num_1 > num_2)
# print(num_1 <= num_2)
# print(num_1 >= num_2)
# print(num_1 == num_2)
# print(num_1 != num_2)




# 2. Assignment Op
"""
=
+=
-=
/=
//=   
*=
%=   
**=
"""
# variable = 11

# num_1 = 11
# num_2 = 5
# print("Num1 is : ",num_1)
# print("Num2 is : ",num_2)
# num_1%=num_2     # num1%num2 = 1  then assign num1=1
# print("Num1 is : ",num_1)
# print("Num2 is : ",num_2)


# 4. Logical Op : 

"""
and :  
    return True if all Equations are True else False.

or : 
    return False if all Equations are False else True.


not :
    return True if Equation is False else False.

"""
# num_1 = 12
# num_2 = 11

# print(num_1>num_2 and num_1!=num_2 and num_1!=12)
# print(num_1<num_2 and num_1!=num_2)
# print(num_1>num_2 and num_1==num_2)
# print(num_1<num_2 and num_1==num_2)


# print(num_1>num_2 or num_1!=num_2)
# print(num_1<num_2 or num_1!=num_2)
# print(num_1>num_2 or num_1==num_2)
# print(num_1<num_2 or num_1==num_2)


# print(num_1>num_2)
# print(not(num_1>num_2))


# True , number (0) ,string ,set,list,
# False , 0 , ""
# print([1] and 12)
# print(11 and 12 and "" and 0 and [1])
# 
# print(0 or 12)









# 5. Identify Op. : 
"""
is 
is not
"""
# num_1 = "12"
# num_2 = "12"


# print(num_1 is num_2)
# print(num_1 is not num_2)



# 6. Membership Op. : 
"""
in 
not in
"""
# num1 = "11"
# num2 = [12,23,11,2]

# print(num1 in num2)
# print(num1 not in num2)


# _. Symbol 
# _. Ternary Op. 


# premitive : non-premitive 


age = int(input("Enter your age : "))

print("Age is",age)


current_year = 2026

print("Birth year : ",current_year-age)