N, B = input().split()
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
N_len = len(N)-1
B = int(B)
result = 0
for i in N:
    if i in alphabet:
        result += (ord(i)-55) * B**N_len
    else:
        result += int(i) * B**N_len
    N_len -= 1
print(result)