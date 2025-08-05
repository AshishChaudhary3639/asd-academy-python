
def factorial(n):
    if n < 0:
        return None
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


def is_even(n):
    return n % 2 == 0
