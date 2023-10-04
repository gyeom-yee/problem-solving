def merge_sort(arr):
    # 크기가 1이하면 반환
    if len(arr) <= 1:
        return arr

    # 리스트를 2분할
    mid = (len(arr)+1) // 2
    left = arr[:mid]
    right = arr[mid:]

    # 2분할한 리스트를 각각 merge sort진행
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)
    return merge(left_sorted, right_sorted)

def merge(left, right):
    i, j = 0, 0
    sorted_list = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            ans.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            ans.append(right[j])
            j += 1

    while i < len(left): # 왼쪽 배열 부분이 남은 경우
        sorted_list.append(left[i])
        ans.append(left[i])
        i += 1
    while j < len(right): # 오른쪽 배열 부분이 남은 경우
        sorted_list.append(right[j])
        ans.append(right[j])
        j += 1
    return sorted_list

n, k = map(int, input().split())
arr = list(map(int, input().split()))
ans = []
merge_sort(arr)
print(ans[k-1] if len(ans) >= k else -1)