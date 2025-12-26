def solution(s, n):
    answer = ""
    for c in s:
        temp = ord(c)
        if c == ' ': answer += ' '
        else:
            if ord('A') <= temp <= ord('Z'):
                if temp+n <= ord('Z'):
                    answer += chr(temp+n)
                else:
                    answer += chr(temp+n-ord('Z')+ord('A')-1)
            elif ord('a') <= temp <= ord('z'):
                if temp+n <= ord('z'):
                    answer += chr(temp+n)
                else:
                    answer += chr(temp+n-ord('z')+ord('a')-1)
    return answer