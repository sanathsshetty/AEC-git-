def generate_fibonacci(n):
    fibonacci_series = []
    a, b = 0, 1
    for _ in range(n):
        fibonacci_series.append(a)
        a, b = b, a + b
    return fibonacci_series


n = 10
fib_series = generate_fibonacci(n)
print(f"Fibonacci series up to {n} numbers: {fib_series}")

#Fibonacci series up to 10 numbers: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
