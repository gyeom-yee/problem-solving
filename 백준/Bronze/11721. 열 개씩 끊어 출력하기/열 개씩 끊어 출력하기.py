word = input()
n = len(word)//10
for i in range(n+1):
    print(word[10*i:10*i+10])