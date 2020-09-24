#平方根を求めるためのニュートン＝ラフソン法
#x**2 - 24 = 0で誤差がepsilonいかになるｘを求める。
epsilon = 0.01
k = 24
guess = k/2.0
numGuesses = 0
while abs(guess*guess - k) >= epsilon:
    guess = guess -(((guess**2) - k)/(2*guess))
    numGuesses+=1
print('Square root of',k,'is about',guess)
print('numGuesses =',numGuesses)
