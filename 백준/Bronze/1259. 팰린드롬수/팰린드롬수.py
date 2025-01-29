while True:
    num_t = input()
    if num_t == '0': break
    print('yes' if num_t == num_t[::-1] else 'no')