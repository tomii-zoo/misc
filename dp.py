# memo[n] = fib(n) の形でメモを取る
memo = {}

# フィボナッチ数列
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    if not n in memo:
        memo[n] = fib(n - 1) + fib(n - 2)
    
    return memo[n]

print(fib(990))
