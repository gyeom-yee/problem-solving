import sys
price = list(map(int, sys.stdin.readlines()))
print(min(price[:3])+min(price[3:])-50)