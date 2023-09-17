import sys
major_sum = 0
grade_sum = 0
score_board = {"A+": 4.5, "A0": 4.0, "B+": 3.5, "B0":3.0, "C+":2.5,"C0":2.0, "D+":1.5, "D0":1.0, "F":0.0}
for _ in range(20):
    subj, credit, grade = sys.stdin.readline().split()
    if grade == "P": continue
    grade_sum += float(credit)
    major_sum += float(credit) * score_board[grade]
print(major_sum/grade_sum)