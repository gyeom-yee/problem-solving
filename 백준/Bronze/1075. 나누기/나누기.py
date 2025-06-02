n = int(input())
f = int(input())

for i in range(n//100*100, n//f*f+f+1):
    if i%f == 0:
        print('0'+str(i%100) if i%100 < 10 else i%100)
        break