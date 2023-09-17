import sys
firm = dict()
for i in range(int(input())):
    name, enter_log = sys.stdin.readline().split()
    if enter_log == "enter": firm[name] = 1
    else: del firm[name]
print("\n".join(sorted(firm.keys(), reverse=True)))