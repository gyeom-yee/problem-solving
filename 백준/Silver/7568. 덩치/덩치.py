n = int(input())
human = []

for _ in range(n):
    x, y = map(int, input().split())
    human.append((x,y))
for i in range(n):
    grade = 1
    for j in range(n):
        if human[i][0] < human[j][0] and human[i][1] < human[j][1]:
            grade += 1
    print(grade, end = ' ')