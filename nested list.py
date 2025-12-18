n = int(input())

students = []   

for _ in range(n):
    name = input()
    grade = float(input())
    students.append([name, grade])  

students.sort(key=lambda x: x[1])
lowest = students[0][1]

for s in students:
    if s[1] != lowest:
        second_lowest = s[1]
        break

names = []

for s in students:
    if s[1] == second_lowest:
        names.append(s[0])

names.sort()

for n in names:
    print(n)
