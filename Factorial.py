def factorial(n):
    if n == 0 or n == 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

for i in range(1, 20):
    print(f"Factorial of {i} is {factorial(i)}")
