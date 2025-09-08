# Factorial
def fac(n):
    if n == 1:
        return 1
    return fac(n - 1)

# Fibonacci
def fib(n):
    if n == 1 or n ==2:
        return 1
    return fib(n - 1) + fib(n - 2)

print(fib(9))