ex = 1000-int(input())
coin = 0
coin += ex//500
ex %= 500
coin += ex//100
ex %= 100
coin += ex//50
ex %= 50
coin += ex//10
ex %= 10
coin += ex//5
ex %= 5
coin += ex//1
ex %= 1
print(coin)