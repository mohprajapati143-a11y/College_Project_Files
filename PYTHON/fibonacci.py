def fibonacci(n):
    # Compute the nth Fibonacci number using recursion.
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# Testing Example
if __name__ == "__main__":
    print("MOHIT PRAJAPATI")
    print("FYCS")
    print("22549")
    n = int(input("Enter the value of n to find the nth Fibonacci number: "))
    print(f"The {n}th Fibonacci number is: {fibonacci(n)}")