import sys
chess = sys.stdin.readlines()
cnt = 0
for row in range(8):
    for col in range(8):
        if row%2==0:
            if col%2==0 and chess[row][col]=='F':
                cnt += 1
        else:
            if col%2!=0 and chess[row][col]=='F':
                cnt += 1
print(cnt)