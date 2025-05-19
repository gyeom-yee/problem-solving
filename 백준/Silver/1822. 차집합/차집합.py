n_a, n_b = map(int, input().split())
a_list = set(map(int, input().split()))
b_list = set(map(int, input().split()))
res = sorted(a_list-b_list)
if res:
    print(len(res), ' '.join(map(str, res)), sep='\n')
else:
    print(0)