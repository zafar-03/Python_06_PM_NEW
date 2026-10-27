my_students = [
    { "rollno" : 1 , "studentname" : "Raj", "course" : "Ai/ML"},
    { "rollno" : 2 , "studentname" : "Rajesh", "course" : "Ui/Ux"},
    { "rollno" : 3 , "studentname" : "Rajendra", "course" : "Web"},
    { "rollno" : 4 , "studentname" : "Rajveer", "course" : "Ai/ML"}
]

# print(my_students)

# add : append 

# my_students.append({"rollno" : 5 , "studentname" : "Sahil", "course" : "Video Editing"})

# my_students.pop(1)
# my_students.remove({"rollno" : 2,"studentname" : "Rajesh", "course" : "Ui/Ux"})

# del my_students[0]

# my_students[0] = { "rollno" : 101 , "studentname" : "Krutarth", "course" : "Web"}

# print(my_students)




# for student in my_students:
#     print(student.get("studentname"))



# students = { 
#     "rollno" : 1 ,
#     "studentname" : "Raj",
#     "course" : "Ai/ML"
# }


courses = {
    "AI/ML" : [
        { "rollno" : 1 , "studentname" : "Raj"},
        { "rollno" : 4 , "studentname" : "Rajveer"}
    ],
    "Web" : [
        { "rollno" : 3 , "studentname" : "Rajendra"}
    ],
    "UI/UX" : []
}
print(courses)
# print(courses)
# for course in courses:
#     print(course,":")
#     for student in courses.get(course):
#         print(student)

courses.get("AI/ML").append( { "rollno" : 3 , "studentname" : "Rajendra"})
# print(courses.update({"AI/ML" : [{"rollno" : 101 , "studentname" : "temp"}]}))

print(courses)
