import sys
cnt = 0
for _ in range(int(input())):
    arr = [0] * 26
    error = 0
    word = sys.stdin.readline().rstrip()
    for i in range(len(word)):
        index = ord(word[i]) - ord('a')
        if word[i-1] == word[i]:
            arr[index] = 0
        elif arr[index] == 1:
            error += 1
            break
        arr[index] = 1
    if error == 0:
        cnt += 1
print(cnt)