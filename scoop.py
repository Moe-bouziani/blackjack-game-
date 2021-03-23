def fact(n):
    result = 1
    if n>1:
        for f in range(2, n+1):
            result *= f
    return result


def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)


def fibonacci(n):
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        n_minus1 = 1
        n_minus2 = 0
        for f in range(1, n):
            result = n_minus2 + n_minus1
            n_minus2 = n_minus1
            n_minus1 = result
    return result


for i in range(36):
    print(i, fibonacci(i))



