students = {'john':["python","django"],"bob":["java","spring"],"jim":["node","react"]}

keys = students.keys()

for eachkey in keys:
    print("Courses taken by ", eachkey, "are ")
    for eachCourse in students[eachkey]:
        print(eachCourse)