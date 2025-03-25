def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


num = int(input("Enter the number : "))
if num < 0:
    print("enter valid factorial")
else:
    print("Factorial of", num, "is", factorial(num))