print("Welcome to Pattern Generator and Number Analyzer!")

while(True):
    print("\nSelect an Option:")
    print("1. Generate Pattern")
    print("2. Analyze range of Numbers")
    print("3. Exit")
    choice = int(input("Enter Your Choice :"))


    match(choice):
        case 1 : print("Case 1")
        case 2 : print("Case 2")
        case 3 : break
        case _ : print("Pease Enter Valid Choice!!")

print("Exiting Program Good bye!")