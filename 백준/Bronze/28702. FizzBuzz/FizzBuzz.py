arr = []
for i in range(3):
    word = input()
    if word.isdigit():
        next_word = int(word)+(3-i)
        if next_word%15 == 0:
            print('FizzBuzz')
        elif next_word%3 == 0:
            print('Fizz')
        elif next_word%5 == 0:
            print('Buzz')
        else:
            print(next_word)
        break