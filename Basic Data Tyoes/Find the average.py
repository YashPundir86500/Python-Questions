n = int(input("Enter number of students :- "))
student_marks = {}
for i in range(n):

    data = input("Enter the name and marks :- ").split()
    name = data[0]
    marks = list(map(float, data[1:]))
    student_marks[name] = marks

query_name = input("Enter student name to find average :- ")

average = sum(student_marks[query_name]) / len(student_marks[query_name])
print("{:.2f}".format(average))

