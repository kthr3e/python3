#fib(5)を求める場合、fib(2)の値が計算される回数を数える。
def fib(n):
    """n>0を整数と仮定
        n番目のふぃぼなち数を返す　"""
    if n==2:
        global count
        count+=1
    if n==0 or n==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def testFib(n):
    for i in range(n+1):
        print('fib of',i,'=',fib(i))

global count
count = 0
fib(5)
print('count =',count)
#広域変数の呼び出し方に注意
