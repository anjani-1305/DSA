def fib(n):
    if n<= 1:
        return n
    else:
        return fib(n-1)+fib(n-2)
a = fib(7)
print(a)