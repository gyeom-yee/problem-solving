import re
board = re.findall(r'X+|\.+', input())
res = []
flag = 0

for i in range(len(board)):
    n = len(board[i])
    if 'X' in board[i]:
        if n < 2 or n%2 != 0:
            flag = 1
            break
        if n%4 == 0:
            board[i] = (n//4)*'AAAA'
        elif n%2 == 0:
            board[i] = (n//4)*'AAAA'+(n%4//2)*'BB'
print(-1 if flag else "".join(board))