num_li = list(map(int, input().split()))
product_sum = 0
for n in num_li:
    product_sum += n*n
print(product_sum%10)