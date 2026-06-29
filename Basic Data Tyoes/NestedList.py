#Given the names and grades for each student in a class of  students, 
# store them in a nested list and print the name(s) of any student(s) having the second lowest grade.


students = []
n = int(input("Enter students :- "))
for i in range(n):
    name = input("Enter Name :- ")
    score = float(input("Enter score :- "))
    students.append([name, score])

scores = sorted(set([student[1] for student in students]))
second_lowest = scores[1]

names = []
for student in students:
    if student[1] == second_lowest:
        names.append(student[0])

for name in sorted(names):
    print(name)


