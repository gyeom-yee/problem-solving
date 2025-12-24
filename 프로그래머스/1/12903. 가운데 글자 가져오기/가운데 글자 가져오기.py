def solution(s):
    l = len(s)
    mid = l//2
    return s[mid] if l%2 else s[mid-1:mid+1]