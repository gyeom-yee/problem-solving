import sys
input = sys.stdin.readline

N = int(input())
students = []
for _ in range(N):
    student = input().split()
    if len(student[2]) < 2:
        student[2] = '0'+student[2]
    if len(student[1]) < 2:
        student[1] = '0'+student[1]
    students.append([int(student[3]+student[2]+student[1]), student[0]])
students.sort()
print(students[-1][1], students[0][1], sep='\n')
