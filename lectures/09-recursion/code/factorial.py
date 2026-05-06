# n >= 1
def factorial(n):
    if n == 1:
        return 1
    else:
        result = factorial(n - 1)
        result *= n
        return result
