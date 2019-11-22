def fib3(N):
    if N <= 3:
        return 1
    else:
        return fib3(N-1) + fib3(N-2) + fib3(N-3)
