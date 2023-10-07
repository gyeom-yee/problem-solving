def hanoi(n, from_pos, by_pos, to_pos):
    if n == 1:
        ans.append(str(from_pos)+" "+str(to_pos))
        return
    hanoi(n-1, from_pos, to_pos, by_pos)
    ans.append(str(from_pos)+" "+str(to_pos))
    hanoi(n-1, by_pos, from_pos, to_pos)

ans = []
hanoi(int(input()), 1, 2, 3)
print(len(ans))
print("\n".join(ans))