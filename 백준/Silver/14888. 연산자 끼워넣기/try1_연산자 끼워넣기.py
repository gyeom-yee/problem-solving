# 첫 시도 without dfs
# 메모리: 36496KB	/ 시간: 960ms
from itertools import permutations
def calculator(x, arr):
    tmp = arr[0]
    for op, val in zip(x, arr[1:]):
        if op == '+': tmp += val
        elif op == '-': tmp -= val
        elif op == '*': tmp *= val
        elif op == '/':
            if tmp < 0:
                tmp = -(-tmp//val)
            else:
                tmp //= val
    return tmp

n = int(input())
arr = list(map(int, input().split()))
operator = list(map(int, input().split()))
operator_li = []
memo = dict()
ans = []

for idx, op in zip(operator, ['+','-','*','/']):
    if idx: operator_li.extend(idx*op)
for x in permutations(operator_li, n-1):
    if x in memo:
        continue
    else:
        tmp = calculator(x, arr)
        memo[x] = tmp
        ans.append(tmp)
print(max(ans), min(ans), sep='\n')
