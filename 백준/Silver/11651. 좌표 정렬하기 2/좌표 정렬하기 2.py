import sys
li = sys.stdin.readlines()[1:]
li.sort(key=lambda x: int(x.split()[0]))
li.sort(key=lambda x: int(x.split()[1]))
sys.stdout.write("".join(li))