def fib(n):
    if n <= 1: return n
    return fib(n-1) + fib(n-2)

# Very slow for n > 30
print(fib(35))