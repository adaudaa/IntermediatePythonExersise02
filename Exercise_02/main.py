import time
import random

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

n = random.randint(15, 35)
start_time = time.time()
result = fibonacci(n)

end_time = time.time()
time_taken = end_time - start_time

print(f"fib({n})={result}")
print(f"fib({n}) Took {time_taken:.6f} seconds")
