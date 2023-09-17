import sys
arr, max_row_index, max_rows= [], [], []
for i in range(9):
    arr.append(list(map(int, sys.stdin.readline().split())))
    max_row_index.append(arr[i].index(m := max(arr[i])))
    max_rows.append(m)
result_max = max(max_rows)
result_max_row = max_rows.index(result_max)
print(result_max)
print(result_max_row+1, max_row_index[result_max_row]+1)