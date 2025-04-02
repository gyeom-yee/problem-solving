import sys
input = sys.stdin.readline

n = int(input())
book_dict = dict()
for _ in range(n):
    title = input().rstrip()
    if title in book_dict:
        book_dict[title] += 1
    else:
        book_dict[title] = 1
top = max(book_dict.values())
result = sorted([key for key, val in book_dict.items() if val == top])
print(result[0])