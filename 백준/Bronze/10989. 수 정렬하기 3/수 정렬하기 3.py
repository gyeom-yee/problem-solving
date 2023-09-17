import sys
count_arr = [0] * 10001
for _ in range(int(input())):
    count_arr[int(sys.stdin.readline())] += 1
for i in range(len(count_arr)):
    for _ in range(count_arr[i]):
        print(i)
