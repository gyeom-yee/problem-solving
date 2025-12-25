def solution(s):
    words = s.split(" ")
    for i, word in enumerate(words):
        words[i] = "".join([c.upper() if i%2==0 else c.lower() for i, c in enumerate(word)])
    return " ".join(words)