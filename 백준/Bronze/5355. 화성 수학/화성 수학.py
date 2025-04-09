import sys
input = sys.stdin.readline
for _ in range(int(input())):
    arr = input().split()
    result = float(arr[0])
    for val in arr[1:]:
        if val == '@':
            result *= 3
        elif val == '%':
            result += 5
        elif val == '#':
            result -= 7
    print('%.2f'%result)