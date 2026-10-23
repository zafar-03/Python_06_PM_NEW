# Nested Loop : 
#  1 loop -> 2 loop 


# for i in range(1,6):                # i = 2
#     print("I :",i,"J :",end="-->")
#     for j in range(1,6):            # j = 1 to 6()
#         print(j,end=" ")
#     print()

# # Pattern : 1
# for i in range(1,6):                # i = 2
#     # print("I :",i,"J :",end="-->")
#     for j in range(1,i+1):            # j = 1 to 6()
#         print(j,end=" ")
#     print()

# Pattern : 2
# for i in range(1,6):                # i = 2
#     # print("I :",i,"J :",end="-->")
#     for j in range(1,i+1):            # j = 1 to 6()
#         print(i,end=" ")
#     print()

# Pattern : 3
# for i in range(1,6):                # i = 2
#     # print("I :",i,"J :",end="-->")
#     for j in range(1,i+1):            # j = 1 to 6()
#         print("*",end=" ")
#     print()


k=1
for i in range(1,5):                
    for j in range(1,i+1):            
        print(k,end=" ")
        k+=1
    print()

"""
1
2 3
4 5 6
7 8 9 10
"""