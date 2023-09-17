import sys
w_dict = dict()
for i in range(int(input())):
    word = sys.stdin.readline().rstrip()
    if word in w_dict: pass
    else: w_dict[word] = len(word)
w_dict = sorted(w_dict.items())
for key, value in sorted(w_dict, key=lambda item: item[1]):
    print(key)