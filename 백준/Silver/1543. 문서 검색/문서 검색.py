import sys
input = sys.stdin.readline

# strip() 으로 \n 는 삭제
doc = input().strip()
up_doc = doc[:]
word = input().strip()
count, start = 0, 0

while 1:
    index = up_doc.find(word)
    if index == -1:
        break
    else:
        up_doc = up_doc[index+len(word):]
        count += 1

print(count)