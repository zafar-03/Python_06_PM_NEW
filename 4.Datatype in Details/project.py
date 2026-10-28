print("Students Data : ")

all_students = []
total = 0
while(True):
    print("\nSelect an Option:")
    print("1. Add Students")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")
    choice = int(input("Enter Your Choice :"))


    match(choice):
        case 1 : 
           total+=1
           all_students.append({
               "GR Id" : (total,),
               "name" : input("Enter Student name :"),
               "age" : int(input("Enter Student Age :")),
               "grade" : input("Enter Student grade :"),
               "subjects" : set(input("Enter subject name (separate with comma) :").split(","))
           }) 
           print("Student added Successfully")
        case 2 : 
            for student in all_students:
                print(student)
        case 3 : print("Case 3")
        case 4 : print("Case 4")
        case 5 : print("Case 5")
        case 6 : break
        case _ : print("Pease Enter Valid Choice!!")

print("Exiting Program Good bye!")




print (set("Maths,Science,Gujarati,Maths".split(",")))