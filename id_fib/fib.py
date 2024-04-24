memo = {}


def fib(n: int, k: int = 1):
    """
    Calculate the nth term of the Fibonacci sequence with a specified step size.

    This function uses memoization to store previously computed values for efficiency.

    Args:
    - n (int): The index of the term to be calculated.
    - k (int): The step size for the Fibonacci sequence (default is 1).

    Returns:
    - int: The value of the nth term in the Fibonacci sequence with step size k.
    """
    args = (n, k)
    if args in memo:
        return memo[args]

    if n == 1:
        ans = 1
    elif n == 2:
        ans = 1
    else:
        ans = fib(n - 1, k) + k * fib(n - 2, k)
    memo[args] = ans
    return ans
