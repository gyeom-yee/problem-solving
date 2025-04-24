word = input()
result = [c for c in word if c not in 'CAMBRIDGE']
print("".join(result))