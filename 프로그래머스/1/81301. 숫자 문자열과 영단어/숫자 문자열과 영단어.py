def solution(s):
    str_n = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i in range(10):
        s = s.replace(str_n[i], str(i))
    return int(s)