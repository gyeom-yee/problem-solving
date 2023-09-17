input()
arr = list(map(int, input().split()))
sorted_arr = sorted(list(set(arr)))
sorted_dict = {k:idx for idx, k in enumerate(sorted_arr)}
print(" ".join(str(sorted_dict[x]) for x in arr))