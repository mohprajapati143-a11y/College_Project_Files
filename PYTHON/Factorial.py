def factorial(n):
    # Compute factorial of n using recursion.
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Testing Example
if __name__ == "__main__":
    print("MOHIT PRAJAPATI")
    print("FYCS")
    print("22549")
    n = int(input("Enter the value of n to find the factorial of number: "))
    print(f"The factorial of {n} is: {factorial(n)}")